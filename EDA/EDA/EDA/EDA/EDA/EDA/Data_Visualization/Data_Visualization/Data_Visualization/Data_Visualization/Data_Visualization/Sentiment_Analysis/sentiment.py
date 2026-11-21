import csv

positive_words = ["good", "great", "excellent", "happy", "amazing", "love"]
negative_words = ["bad", "poor", "worst", "sad", "terrible", "hate"]

with open("Sentiment_Analysis/reviews.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    with open("Sentiment_Analysis/sentiment_results.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["Review", "Sentiment"])

        for row in reader:
            review = row["Review"].lower()

            if any(word in review for word in positive_words):
                sentiment = "Positive"
            elif any(word in review for word in negative_words):
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            writer.writerow([row["Review"], sentiment])

print("Sentiment analysis completed!")
