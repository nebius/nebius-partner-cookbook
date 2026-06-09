# Goodreads datasets

These files are large and are not committed to the repository.
They are referenced here for educational, non-commercial experimentation only.
See [`../TRADEMARK.md`](../TRADEMARK.md) for the dataset notice.

Download them from the UCSD Goodreads Book Graph dataset page:

https://cseweb.ucsd.edu/~jmcauley/datasets/goodreads.html#datasets

The direct files you want for this repo are:

- `goodreads_books.json.gz`
- `goodreads_book_authors.json.gz`
- `goodreads_book_works.json.gz`
- `goodreads_book_genres_initial.json.gz`

From the dataset mirror, they live under:

https://mcauleylab.ucsd.edu/public_datasets/gdrive/goodreads/

## Download

```bash
mkdir -p data
cd data

curl -O https://mcauleylab.ucsd.edu/public_datasets/gdrive/goodreads/goodreads_books.json.gz
curl -O https://mcauleylab.ucsd.edu/public_datasets/gdrive/goodreads/goodreads_book_authors.json.gz
curl -O https://mcauleylab.ucsd.edu/public_datasets/gdrive/goodreads/goodreads_book_works.json.gz
curl -O https://mcauleylab.ucsd.edu/public_datasets/gdrive/goodreads/goodreads_book_genres_initial.json.gz
```

## Verify

```bash
gzip -t goodreads_books.json.gz
gzip -t goodreads_book_authors.json.gz
gzip -t goodreads_book_works.json.gz
gzip -t goodreads_book_genres_initial.json.gz
```

## Notes

- The files are newline-delimited JSON inside gzip archives.
- They are academic datasets from UCSD and are large enough that they should stay out of git.
- If you only need book vectors for Pinecone, `goodreads_books.json.gz` is the primary file.
