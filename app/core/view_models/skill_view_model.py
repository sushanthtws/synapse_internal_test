class SkillViewModel:
    """
    Standard UI contract for all skills.
    Every skill MUST be rendered using this format.
    """

    def __init__(self, skill: dict):
        self.skill = skill

    def to_ui(self) -> dict:
        return {
            "header": self._header(),
            "subheader": self._subheader(),
            "body": self._body(),
            "tags": self._tags()
        }

    def _header(self):
        return self.skill.get("title", "Untitled Skill")

    def _subheader(self):
        summary = self.skill.get("summary", "")
        return summary[:140] + "..." if len(summary) > 140 else summary

    def _body(self):
        return self.skill.get("raw_markdown", "")

    def _tags(self):
        return self.skill.get("tags", [])