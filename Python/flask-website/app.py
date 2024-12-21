from flask import Flask, request, render_template, send_file
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_rss', methods=['POST'])
def generate_rss():
    # Get the RSS feed URL from the form
    rss_url = request.form['rss_url']

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Check if the feed was parsed successfully
    if feed.bozo:
        return "Invalid RSS feed URL. Please try again.", 400

    new_rss = f"""<?xml version="1.0" encoding="UTF-8"?>
    <rss version="2.0">
      <channel>
        <title>{feed.feed.title}</title>
        <link>{feed.feed.link}</link>
        <description>{feed.feed.description}</description>
        <language>{feed.feed.language}</language>
    """

    # Add each entry in the existing RSS feed to the new RSS feed
    for entry in feed.entries:
        new_rss += f"""
        <item>
          <title>{entry.title}</title>
          <link>{entry.link}</link>
          <description>{entry.description}</description>
          <pubDate>{entry.published}</pubDate>
        </item>
        """

    # Close the new RSS feed
    new_rss += """
      </channel>
    </rss>"""

    # Save the new RSS feed to a file
    filename = "new_rss.xml"
    with open(filename, "w") as f:
        f.write(new_rss)

    return f"RSS feed generated successfully! You can download it <a href='/download/{filename}'>here</a>.", 200

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)