class ReportRenderer:
    """
    Displays a validation report in a readable format.
    """

    def display(self, report: dict):

        print("=" * 60)
        print("Validation Report")
        print("=" * 60)

        print(f"Dataset         : {report['dataset']}")
        print(f"Generated At    : {report['generated_at']}")

        print()

        print(f"Total Rows      : {report['total_rows']}")
        print(f"Valid Rows      : {report['valid_rows']}")
        print(f"Invalid Rows    : {report['invalid_rows']}")

        print()

        print(f"Quality Score   : {report['quality_score']}%")

        print("\nValidation Rules")
        print("-" * 60)

        for rule, count in report["rules"].items():
            print(f"{rule:<25}: {count}")