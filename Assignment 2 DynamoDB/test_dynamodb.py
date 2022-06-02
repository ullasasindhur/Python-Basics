import pytest
import dynamodb


@pytest.mark.parametrize(
    "input,output",
    [
        ({"Items": []}, "Nothing Found with the Artist Name"),
        (
            {"Items": [{"Artist": "Sindhur", "SongTitle": "Ullasa"}]},
            [{"Artist": "Sindhur", "SongTitle": "Ullasa"}],
        ),
        (
            {
                "Items": [
                    {"Artist": "Sindhur", "SongTitle": "Ullasa"},
                    {"Artist": "Sindhur", "SongTitle": "a"},
                    {"Artist": "Sindhur", "SongTitle": "z"},
                ]
            },
            [
                {"Artist": "Sindhur", "SongTitle": "z"},
                {"Artist": "Sindhur", "SongTitle": "a"},
                {"Artist": "Sindhur", "SongTitle": "Ullasa"},
            ],
        ),
        ({}, "Error Occured in query artist"),
        (
            {"Items": [{"artist": "Sindhur", "songTitle": "Ullasa"}]},
            "Error Occured in query artist",
        ),
    ],
)
def test_query_artist(monkeypatch, input, output):
    monkeypatch.setattr("dynamodb.query_table", lambda x: input)
    assert dynamodb.query_artist("Artist") == output


def test_query_artist_exception(monkeypatch):
    def query(x):
        raise Exception

    monkeypatch.setattr("dynamodb.query_table", query)
    assert dynamodb.query_artist("Artist") == "Error Occured in query artist"
