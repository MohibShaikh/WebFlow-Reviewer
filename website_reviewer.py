"""
WebFlow Reviewer
---------------
A lightning-fast, keyboard-driven tool for efficiently reviewing and categorizing websites.
Perfect for content moderators, SEO specialists, and web researchers.

Author: Mohib Shaikh
License: MIT
"""

import pandas as pd
import webbrowser
import keyboard
import time
from datetime import datetime
import os
import sys

class WebsiteReviewer:
    def __init__(self):
        self.reviewed_count = 0
        self.total_count = 0
        self.results = {'good': 0, 'bad': 0}

    def validate_csv(self, input_file):
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found")
            return False
        if not input_file.endswith('.csv'):
            print("Error: File must be a CSV file")
            return False
        return True

    def review_websites(self, input_file):
        if not self.validate_csv(input_file):
            return

        try:
            df = pd.read_csv(input_file)
            if 'url' not in df.columns:
                print("Error: CSV file must have a 'url' column")
                return
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return

        df['review'] = 'pending'
        self.total_count = len(df)
        
        self.print_instructions()

        for index, row in df.iterrows():
            url = row['url']
            self.print_progress(index, url)
            
            try:
                webbrowser.open(url)
            except Exception as e:
                print(f"Error opening URL: {e}")
                continue
            
            if self.get_user_input(df, index):
                break

        self.save_results(df)
        self.print_summary()

    def print_instructions(self):
        print("\n🌐 Website Review Process Started!")
        print("Controls:")
        print("  👍 Press 'y' for good websites")
        print("  👎 Press 'n' for bad websites")
        print("  ⏹️  Press 'q' to quit the process")
        print("  ⏭️  Press 's' to skip current website\n")

    def print_progress(self, index, url):
        print(f"\n[{index + 1}/{self.total_count}] Opening: {url}")
        print("Waiting for your review...")

    def get_user_input(self, df, index):
        while True:
            if keyboard.is_pressed('y'):
                df.at[index, 'review'] = 'good'
                self.results['good'] += 1
                self.reviewed_count += 1
                time.sleep(0.3)
                break
            elif keyboard.is_pressed('n'):
                df.at[index, 'review'] = 'bad'
                self.results['bad'] += 1
                self.reviewed_count += 1
                time.sleep(0.3)
                break
            elif keyboard.is_pressed('s'):
                print("Skipped website")
                time.sleep(0.3)
                break
            elif keyboard.is_pressed('q'):
                print("\nProcess interrupted by user")
                return True
            time.sleep(0.1)
        return False

    def save_results(self, df):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f'website_reviews_{timestamp}.csv'
        df.to_csv(output_file, index=False)
        print(f"\n📊 Results saved to: {output_file}")

    def print_summary(self):
        print("\n📈 Review Summary:")
        print(f"Total websites reviewed: {self.reviewed_count}/{self.total_count}")
        print(f"Good websites: {self.results['good']}")
        print(f"Bad websites: {self.results['bad']}")
        print(f"Skipped: {self.total_count - self.reviewed_count}")

def main():
    print("🌐 Website Review Tool")
    print("=====================")
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = input("Enter the path to your CSV file: ")
    
    reviewer = WebsiteReviewer()
    reviewer.review_websites(input_file)

if __name__ == "__main__":
    main()
