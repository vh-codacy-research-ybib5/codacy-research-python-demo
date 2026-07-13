import os


def greet(name: str) -> str:
    return f"hello {name}"


def read_optional_env() -> str:
    return os.environ.get("CODACY_RESEARCH_DEMO", "unset")


if __name__ == "__main__":
    print(greet("codacy"))
