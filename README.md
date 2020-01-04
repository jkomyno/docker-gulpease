<h1 align="center">docker-gulpease</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/jkomyno/docker-gulpease#readme">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/jkomyno/docker-gulpease/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
</p>

> Docker-ready Python utility for evaluating the Gulpease Index of one or more PDF documents.

## 🔑 Key features

* 🥇 supports multiple PDF files at once
* ✨ runs on Docker by default
* 💪 supports both restrictive and not restrictive Gulpease Index evaluation
* ✔️ clear and easily parsable JSON output

## 🚀 Description

The *Gulpease Index* is a measure that calculates the readability of a text based on the length of words (measured in number of letters), the number of words and the length of sentences. This index is based off the Italian language.

`docker-gulpease` is an opinionated Python 3 utility executed in a Docker environment that
offers an easy way to . Given a number of PDF documents in the same folder,
it produces a JSON report with the measurement results.

## ❔ How to use

Using `docker-gulpease` is fast, practical and easy. Just follow these simple steps:

1. Put your PDF documents in the [`./pdf`](./pdf) folder.
2. Execute the [`./run.sh`](./run.sh) script in a Bash like environment (for Windows, you can use Git Bash).
3. Read the report from the terminal or from [`./report/report.json`](./report/report.json).

## Report Structure

The JSON report contains an array of objects with the following keys:

* `filename`: Name of the PDF file read from the [`./pdf`](./pdf) folder.
* `index`: Gulpease restrictive index evaluation.
* `letters`: Number of letters in the document.
* `non_restrictive_index`: Non restrictive version of the Gulpease index.
* `points`: Number of point-like symbols (`.`, `,`, etc.).
* `words`: Number of words in the document.

Here's an example of a [`./report/report.json`](./report/report.json) file:

```json
[
    {
        "filename": "Candidatura ERASMUS.pdf",
        "index": 87.36996336996337,
        "letters": 298,
        "non_restrictive_index": 90.94139194139194,
        "points": 4,
        "words": 1092
    },
    {
        "filename": "Elenco Attività Estero.pdf",
        "index": 22.803278688524586,
        "letters": 2139,
        "non_restrictive_index": 26.73770491803279,
        "points": 4,
        "words": 305
    }
]
```

## 💪 Docker Dependencies

Docker version should be at least `v17.06.0+`.

- **[python](https://hub.docker.com/_/python?tab=description):3.7-alpine**: minimal Python 3.7 container for Alpine Linux.
- **[kalledk/pdftotext](https://hub.docker.com/r/kalledk/pdftotext)**: converts PDF files to plain text.

## 👤 Author

**Alberto Schiabel**

* Github: [@jkomyno](https://github.com/jkomyno)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/jkomyno/react-native-user-inactivity/issues).

How can this project be improved? For instance, the PDF files could be dragged over a web application and the JSON report could be generated for download.
Such an improvement is not discouraged, but I think it would be overwhelming for
the purpose of this small project.

If you have any doubt or suggestion, please open an issue.

## 🦄 Show your support

Give a ⭐️ if this project helped or inspired you!

## 📝 License

Built with ❤️ by [Alberto Schiabel](https://github.com/jkomyno).<br />
This project is [MIT](https://github.com/jkomyno/docker-gulpease/blob/master/LICENSE) licensed.

## Related repositories

* [`kalledk/pdftotext`](https://github.com/KaDock/pdftotext)
