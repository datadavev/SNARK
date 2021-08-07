import pytest
import snark

test_arks = [
    [
        "https://example.org/ARK:12345/x54xz321//..//s3/f8.05v.tiff",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
        snark.Inflection.NONE,
    ],
    [
        "https://example.org/ARK:12345/x54xz321/s3/f8.05v.tiff",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
        snark.Inflection.NONE,
    ],
    [
        "https://example.org/ark:12345/x54xz321/s3?test=1",
        "ark:12345/x54xz321/s3",
        snark.Inflection.NONE,
    ],
    [
        "https://example.org/ark:12345/x54xz321/%23%40/",
        "ark:12345/x54xz321/#@/",
        snark.Inflection.NONE,
    ],
    [
        "https://example.org/ARK:12-3-45/x54-xz-321/s3/f8.05v.tiff",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
        snark.Inflection.NONE,
    ],
    [
        "https://example.org/ARK:12345/x54xz321/s3/f8.05v.tiff%3F",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
        snark.Inflection.METADATA,
    ],
    [
        "https://example.org/ARK:12345/x54xz321/s3/f8.05v.tiff%3F%3F",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
        snark.Inflection.POLICY,
    ],
]


@pytest.mark.parametrize("src,ex_ark, ex_inf", test_arks)
def test_normalize(src, ex_ark, ex_inf):
    ark, inflection = snark.normalizeARK(src)
    assert ark[-1] == ex_ark
    assert inflection == ex_inf
