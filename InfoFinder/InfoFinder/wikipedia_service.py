import wikipediaapi

class WikipediaService:
    def __init__(self, language='en', summary_length=500):
        self.wiki_wiki = wikipediaapi.Wikipedia(
            language=language,
            user_agent='InfoFinder (https://github.com/nevermore-rgb/InfoFinder)'
        )
        self.summary_length = summary_length

    def get_summary(self, title):
        page = self.wiki_wiki.page(title)
        if page.exists():
            summary = page.summary
            if len(summary) > self.summary_length:
                summary = summary[:self.summary_length] + "..."
            return summary
        else:
            return f"No summary found for {title}"
