import json
import os
from scholarly import scholarly
import datetime

def update_stats():
    # Author ID from environment variable or default
    author_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'edyJPQQAAAAJ')
    
    print(f"Fetching data for author: {author_id}")
    try:
        author = scholarly.search_author_id(author_id)
        author = scholarly.fill(author, sections=['counts', 'publications'])
        
        # Prepare the main data
        data = {
            "name": author.get('name'),
            "citedby": author.get('citedby', 0),
            "updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "publications": {}
        }
        
        for pub in author.get('publications', []):
            pub_id = pub.get('author_pub_id')
            if pub_id:
                data["publications"][pub_id] = {
                    "num_citations": pub.get('num_citations', 0),
                    "title": pub.get('bib', {}).get('title'),
                    "author_pub_id": pub_id
                }
        
        # Save to gs_data.json
        stats_dir = 'google-scholar-stats'
        if not os.path.exists(stats_dir):
            os.makedirs(stats_dir)
            
        with open(os.path.join(stats_dir, 'gs_data.json'), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        # Save to gs_data_shieldsio.json for the total citations badge
        shields_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(data["citedby"])
        }
        with open(os.path.join(stats_dir, 'gs_data_shieldsio.json'), 'w', encoding='utf-8') as f:
            json.dump(shields_data, f, indent=2, ensure_ascii=False)
            
        print("Successfully updated Google Scholar stats.")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    update_stats()
