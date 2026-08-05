from edqp.validation.rules.null_rule import NullRule
from edqp.validation.rules.duplicate_rule import DuplicateRule
from edqp.validation.rules.email_rule import EmailRule
from edqp.validation.rules.range_rule import RangeRule


class RuleRegistry:
    """
    Creates validation rules from configuration.
    """

    def __init__(self):

        self.rule_map = {
            "null": NullRule,
            "duplicate": DuplicateRule,
            "email": EmailRule,
            "range": RangeRule,
        }

    def register(self, validation_engine, validation_config):

        for rule in validation_config["rules"]:

            rule_type = rule["type"]

            rule_class = self.rule_map.get(rule_type)

            if rule_class is None:
                raise ValueError(
                    f"Unknown validation rule: {rule_type}"
                )

            kwargs = {
                key: value
                for key, value in rule.items()
                if key not in ["name", "type"]
            }

            validation_engine.add_rule(
                name=rule["name"],
                rule=rule_class(),
                **kwargs,
            )

        return validation_engine