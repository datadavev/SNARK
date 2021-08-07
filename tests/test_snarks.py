import pytest
import snark

test_arks = [
    [
        "https://example.org/ARK:12345/x54xz321//..//s3/f8.05v.tiff",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
    ],
    [
        "https://example.org/ARK:12345/x54xz321/s3/f8.05v.tiff",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
    ],
    ["https://example.org/ark:12345/x54xz321/s3?test=1", "ark:12345/x54xz321/s3"],
    ["https://example.org/ark:12345/x54xz321/%23%40/", "ark:12345/x54xz321/#@/"],
    [
        "https://example.org/ARK:12-3-45/x54-xz-321/s3/f8.05v.tiff",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
    ],
    [
        "https://example.org/ARK:12345/x54xz321/s3/f8.05v.tiff%3F",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
    ],
    [
        "https://example.org/ARK:12345/x54xz321/s3/f8.05v.tiff%3F%3F",
        "ark:12345/x54xz321/s3/f8.05v.tiff",
    ],
]


@pytest.mark.parametrize("src,expected", test_arks)
def test_normalize(src, expected):
    ark, inflection = snark.normalizeARK(src)
    assert ark[-1] == expected
