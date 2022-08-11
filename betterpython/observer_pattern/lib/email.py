def send_email(name: str, address: str, subject: str, body: str) -> None:
    print(f"Sending email to {name} ({address})")
    print("=========")
    print(f"Subject: {subject}\n")
    print(body)
