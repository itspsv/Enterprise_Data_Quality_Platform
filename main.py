from edqp.config.config_loader import ConfigLoader


def main():
    config = ConfigLoader().get()

    print("=" * 50)
    print(config["project"]["name"])
    print("Version:", config["project"]["version"])
    print("AWS Region:", config["aws"]["region"])
    print("Raw Data Path:", config["paths"]["raw"])
    print("=" * 50)


if __name__ == "__main__":
    main()