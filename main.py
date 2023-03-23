import json
from database import DatabaseData
from datetime import datetime

db = DatabaseData()

with open('data/data2.txt', 'r') as f:
    json_data = f.read().split('\n')
    for data in json_data:
        try:
            json_object = json.loads(data)
            print(json_object)



            data = {
                'first_name': json_object['first_name'],
                'last_name': json_object['last_name'],
                'emails': json_object['emails'],
                'phone_numbers': json_object['phone_numbers'],
                'gender': json_object['gender'],
                'birth_year': json_object['birth_year'],
                'linkedin_url': json_object['linkedin_url'],
                'facebook_url': json_object['facebook_url'],
                'twitter_url': json_object['twitter_url'],
                'twitter_username': json_object['twitter_username'],
                'github_url': json_object['github_url'],
                'github_username': json_object['github_username'],
                'work_email': json_object['work_email'],
                'mobile_phone': json_object['mobile_phone'],
                'industry': json_object['industry'],
                'job_title': json_object['job_title'],
                'job_title_role': json_object['job_title_role'],
                'job_company_name': json_object['job_company_name'],
                'job_company_linkedin_url': json_object['job_company_linkedin_url'],
                'job_company_location_name': json_object['job_company_location_name'],
                'job_summary': json_object['job_summary'],
                'location_name': json_object['location_name'],
                'location_region': json_object['location_region'],
                'location_country': json_object['location_country'],
                'location_continent': json_object['location_continent'],
                'summary': json_object['summary']
            }

            db.insert_data(data)

        except json.decoder.JSONDecodeError:
            pass

