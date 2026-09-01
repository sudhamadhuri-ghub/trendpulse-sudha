headers = {"User-Agent": "TrendPulse/1.0"}
hacker_news_url ='https://hacker-news.firebaseio.com/v0/topstories.json'

keywords = {
    "technology": ['AI','software','tech','code','computer','data','cloud','API','GPU','LLM'],
    "worldnews": ['war','government','country','president','election','climate','attack','global'],
    "sports": ['NFL','NBA','FIFA','sport','game','team','player','league','championship'],
    "science": ['research','study','space','physics','biology','discovery','NASA','genome'],
    "entertainment": ['movie','film','music','Netflix','game','book','show','award','streaming']
}

def find_category(title):
    """Find the category based on keywords in the title."""

    title = title.lower()

    for category, words in keywords.items():
        for word in words:
            if word.lower() in title:
                return category

    return None

story_details_url = 'https://hacker-news.firebaseio.com/v0/item/{id}.json'

stories = []
category_limits = {} # To store counts for each category
max_stories_per_category = 25 # limits max stories per category
max_total_stories = 125 # limits max all category stories
total_stories_collected = 0 # counts total stories collected

if story_ids:
    for i, story_id in enumerate(story_ids):
        if total_stories_collected >= max_total_stories:
            break # Stop if we've collected enough total stories

        story_url = story_details_url.format(id=story_id)
        response = requests.get(story_url, headers=headers)
        if response.status_code == 200:
            story_data = response.json()
            if story_data and 'title' in story_data: # consider only stories with title
                category = find_category(story_data.get('title', ''))

                if category is not None: #categories other than specifies were skipped
                    # Initialize category count if not present
                    category_limits.setdefault(category, 0)

                    if category_limits[category] < max_stories_per_category:
                        story_entry = {
                            'post_id': story_data.get('id'),
                            'title': story_data.get('title'),
                            'category': category, # Use the found category
                            'score': story_data.get('score'),
                            'num_comments': story_data.get('descendants', 0),
                            'author': story_data.get('by'),
                            'collected_at': datetime.now().isoformat()
                        }
                        stories.append(story_entry)
                        category_limits[category] += 1
                        total_stories_collected += 1
                # If category is None or category limit reached, skip this story
        else:
            continue #if not able to fetch story data go to next story Id