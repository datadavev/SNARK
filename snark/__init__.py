"""
SNARK implements lexical normalization for ARK identifiers.

ARK Spec:
  https://datatracker.ietf.org/doc/html/draft-kunze-ark-27
"""

import re
import urllib.parse
import logging
import enum

# (^ark:)([1-9bcdfghjkmnpqrstvwxz][0-9bcdfghjkmnpqrstvwxz]{4})(/[a-zA-Z0-9\=\~\*\+\@\_\$]{2,128})([a-zA-Z0-9\=\~\*\+\@\_\$\.\/]*)
RE_ARK = re.compile(
    (
        r"(^ark:)"
        r"([1-9bcdfghjkmnpqrstvwxz][0-9bcdfghjkmnpqrstvwxz]{4})"
        r"/([a-zA-Z0-9\=\~\*\+\@\_\$]{2,128})"
        r"([a-zA-Z0-9\=\~\*\+\@\_\$\.\/]*)"
    )
)


class Inflection(enum.Enum):
    NONE = 1
    METADATA = 2
    POLICY = 3


def piecesOfARK(ark):
    """

    Args:
        ark: normalized ARK

    Returns:
        dict {valid:T/F, naan, shoulder, remainder)

    """
    res = {"valid": False, "naan": None, "name": None, "qualifier": None}
    mtch = RE_ARK.match(ark)
    if not mtch:
        return res
    res["valid"] = True
    res["naan"] = mtch.group(2)
    res["name"] = mtch.group(3)
    res["qualifier"] = mtch.group(4)
    return res


def normalizeARK(uark, inflection_char="?"):
    inflection = Inflection.NONE
    res = [
        uark.strip(),
    ]
    # 1. The NMA part (eg, everything from an initial "https://" up to the
    # next slash), if present is removed.
    res.append(re.sub(r"(^https?\://.*/)(ark:)", r"\2", res[-1], flags=re.I))
    logging.debug("01: %s", res[-1])

    # 2. Any URI query string is removed (everything from the first
    # literal '?' to the end of the string).
    res.append(re.sub(r"\?.*$", "", res[-1], flags=re.I))
    logging.debug("02: %s", res[-1])

    # 3. The first case-insensitive match on "ark:/" or "ark:" is
    # converted to "ark:" (replacing any upper case letters and
    # removing any terminal '/')
    res.append(re.sub(r"ark:/*", "ark:", res[-1], flags=re.I))
    logging.debug("03: %s", res[-1])

    # 4. In the string that remains, the two characters following every
    # occurrence of `%' are converted to lower case. The case of all
    # other letters in the ARK string must be preserved
    _ark = urllib.parse.unquote(res[-1])
    # white space may be percent encoded
    res.append(_ark.strip())
    logging.debug("04: %s", res[-1])

    # 5. All hyphens are removed.
    res.append(re.sub(r"-", "", res[-1]))
    logging.debug("05: %s", res[-1])

    # 6. If normalization is being done as part of a resolution step, and
    # if the end of the remaining string matches a known inflection,
    # the inflection is noted and removed.
    #
    # Inflection is indicated by "?" or "??", however these characters
    # are removed in step 3 unless they have been percent escaped
    _ark = res[-1]
    if _ark[-2:] == inflection_char * 2:
        inflection = Inflection.POLICY
        _ark = _ark[:-2]
    elif _ark[-1:] == inflection_char:
        inflection = Inflection.METADATA
        _ark = _ark[:-1]
    res.append(_ark)
    logging.debug("06: %s", res[-1])

    # 7. Structural characters (slash and period) are normalized: initial
    # and final occurrences are removed, and two structural characters
    # in a row (e.g., // or ./) are replaced by the first character,
    # iterating until each occurrence has at least one non-structural
    # character on either side.
    _ark = re.sub(r"(/[/\.]+)", r"/", res[-1])
    _ark = re.sub(r"\.[\./]+", r".", _ark)
    res.append(_ark)
    logging.debug("07: %s", res[-1])

    # 8. If there are any components with a period on the left and a slash
    # on the right, either the component and the preceding period must
    # be moved to the end of the Name part or the ARK must be thrown
    # out as malformed.
    logging.debug("08: %s", res[-1])

    return res, inflection
