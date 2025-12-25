"""
Generate Synthetic Support Case Data - Enhanced Version
Mimics the actual data structure with realistic patterns
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Set seed for reproducibility
np.random.seed(42)

# Configuration
n_cases = 1200

# Define realistic distributions based on actual data structure
regions = ['APAC', 'EMEA', 'Americas']
region_weights = [0.35, 0.35, 0.30]

priorities = ['Critical', 'Major', 'Minor', 'Informational']
priority_weights = [0.10, 0.50, 0.30, 0.10]

severities_map = {
    'Critical': ['High (Critical)'],
    'Major': ['Medium (Major)', 'High (Major)'],
    'Minor': ['Low (Minor)', 'Medium (Minor)'],
    'Informational': ['Low (Minor)']
}

screen_status = ['UP', 'DOWN', 'Please Specify']
screen_status_weights = [0.85, 0.10, 0.05]

case_status = ['Solving', 'Under Review', 'Resolved', 'Closed']
case_status_weights = [0.40, 0.25, 0.25, 0.10]

states = ['Solving', 'Under Review', 'Pending Resolution', 'Closed']

types = ['Email Request', 'Web Support', 'Phone Call']
type_weights = [0.70, 0.20, 0.10]

categories = [
    'Projector', 'Audio', 'Screen / Masking', 'Automation',
    'Screen Corridor', 'Facility', 'Qalif', 'Network'
]

reported_issues = [
    'IMAGE GEOMETRY/ALIGNMENT ISSUE', 'Laser Module Driver Warning',
    'NO IMAGE', 'INTERMITTENT AUDIO', 'Hardware Issues',
    'PLAYBACK STOPPED UNEXPECTEDLY', 'Disk Capacity Warning',
    'CAN NOT POWER-UP COMPONENT', 'Booth Audio Monitor Issue',
    'Network Connectivity Issue', 'Color Calibration Required',
    'IMAGE DISCOLORATION', 'IMPROPER AUDIO LEVEL', 'TPC Display Issue',
    'Software Not Responding', 'Application Not Responding',
    'Screen Shaker Vibration', 'UPS Issue', 'Content Update Request',
    'Auditorium Lighting Issue', 'Booth Temperature Issue'
]

resolutions = [
    'Pending Resolution', 'Replaced Component', 'Power cycled / Reboot Server',
    'Adjusted Settings', 'Replaced UPS Batteries', 'Software Update Applied',
    'Hardware Replaced', 'Recalibrated System', 'Firmware Updated',
    'Network Configuration Fixed', 'Replaced Qalif'
]

queue_names = [
    'EMEA Issues', 'EMEA Dispatched', 'Americas Issues', 'CSE Dispatched',
    'APAC Issues', 'APAC Dispatched', '3rd Party Issues', 'Customer Managed',
    'Future Work', 'EM3 Issues'
]

# Site names by region
sites_apac = [
    'CGV Shanghai Fudi', 'CGV Beijing Wanda', 'CGV Seoul Gangnam',
    'Wanda Changsha', 'Wanda Jiaxing', 'Wanda Shanghai Darongcheng',
    'Wanda Chengdu Wuhou', 'Wanda XiAn Gaoxin',
    'Golden Harvest Hong Kong', 'SF Cinema Tokyo',
    'Lotte Cinema Seoul', 'Major Cineplex Bangkok'
]

sites_emea = [
    'Vue Eindhoven', 'Vue Hilversum', 'Vue London Leicester Square',
    'Odeon Thorpe Park', 'Odeon Leicester Square',
    'Pathe Rouen Docks 76', 'Pathe Belle Epine - Thiais',
    'Pathe Gaumont Rennes', 'Pathe Massy', 'Pathe Nice Gare Du Sud',
    'Cineworld Birmingham', 'Kinopolis Munich',
    'KNCC Cinescape Avenues', 'Muvi Mall of Dhahran'
]

sites_americas = [
    'AMC Empire 25 - 0552', 'AMC Lincoln Square 13 - 2310',
    'AMC Mission Valley 20 - 0246', 'AMC Jersey Gardens 20 - 2198',
    'AMC Staten Island Mall 11 - 0558', 'AMC Newport On The Levee 20 - 0665',
    'AMC Dine-In Thoroughbred 20 - 4457',
    'Cinemark Century City', 'Cinemark Playa Vista',
    'Regal LA Live', 'Dolby Burbank Umlang', 'Dolby Headquarters 1'
]

markets_apac = [
    'Market-China-CGV', 'Market-Korea', 'Market-Japan',
    'Market-Hong Kong', 'Market-Singapore', 'Market-Thailand'
]

markets_emea = [
    'Market-Netherlands-CN-CDS-VG', 'Market-UK-CDS-VUK-CDS',
    'Market-France-ADDE-CDS', 'Market-Kuwait', 'Market-Germany',
    'Market-Saudi Arabia'
]

markets_americas = [
    'Market-NY', 'Market-CA', 'Market-SAD', 'Market-LA',
    'Market-NJ', 'Market-COLOH', 'Market-NSH', 'Market-SAF'
]

all_sites = {'APAC': sites_apac, 'EMEA': sites_emea, 'Americas': sites_americas}
all_markets = {'APAC': markets_apac, 'EMEA': markets_emea, 'Americas': markets_americas}

# Generate dataset
data = []

for i in range(n_cases):
    # Basic identifiers
    dat_id = 1880000 + i
    region = np.random.choice(regions, p=region_weights)
    site_name = np.random.choice(all_sites[region])
    market = np.random.choice(all_markets[region])

    # Status fields
    status = np.random.choice(case_status, p=case_status_weights)
    priority = np.random.choice(priorities, p=priority_weights)
    severity = np.random.choice(severities_map[priority])
    screen_stat = np.random.choice(screen_status, p=screen_status_weights)

    # Extract state from actual data (state is often in US states for Americas)
    if region == 'Americas':
        states_us = ['CA', 'NY', 'NJ', 'TX', 'TN', 'KY', 'OH']
        state = np.random.choice(states_us)
    else:
        # For EMEA/APAC, use country names
        if region == 'EMEA':
            state = np.random.choice(['France', 'England', 'Netherlands', 'Kuwait', 'Germany'])
        else:
            state = np.random.choice(['China', 'Korea', 'Japan', 'Singapore', 'Thailand'])

    case_stat = status  # Often same as status
    type_req = np.random.choice(types, p=type_weights)
    category = np.random.choice(categories)
    reported_issue = np.random.choice(reported_issues)
    resolution = np.random.choice(resolutions)

    # Queue assignment based on region
    if region == 'EMEA':
        queue = np.random.choice(['EMEA Issues', 'EMEA Dispatched', 'Future Work'])
    elif region == 'APAC':
        queue = np.random.choice(['APAC Issues', 'APAC Dispatched'])
    else:
        queue = np.random.choice(['CSE Dispatched', '3rd Party Issues', 'Customer Managed', 'EM3 Issues'])

    # Time calculations
    if priority == 'Critical':
        base_time = np.random.lognormal(2.5, 0.8)
    elif priority == 'Major':
        base_time = np.random.lognormal(3.0, 0.7)
    elif priority == 'Minor':
        base_time = np.random.lognormal(2.0, 0.6)
    else:
        base_time = np.random.lognormal(3.2, 0.9)

    # Regional multipliers
    if region == 'APAC':
        regional_multiplier = 0.85
    elif region == 'EMEA':
        regional_multiplier = 1.15
    else:
        regional_multiplier = 1.05

    resolution_time_days = int((base_time * regional_multiplier) / 24)

    # Add outliers
    if np.random.random() < 0.05:
        resolution_time_days *= np.random.randint(3, 8)

    # Generate dates
    days_ago = np.random.randint(30, 365)
    creation_date = datetime.now() - timedelta(days=days_ago)
    last_update_date = creation_date + timedelta(days=resolution_time_days)

    # Format dates like the actual data (M/D/YYYY H:MM)
    creation_time = creation_date.strftime('%-m/%-d/%Y %-H:%M')
    last_update_time = last_update_date.strftime('%-m/%-d/%Y %-H:%M')

    data.append({
        'Dat': dat_id,
        'Site Name': site_name,
        'Status': status,
        'Priority': priority,
        'Severity': severity,
        'Screen Status': screen_stat,
        'State': state,
        'Case status': case_stat,
        'Type': type_req,
        'Category': category,
        'Reported Issue': reported_issue,
        'Resolution': resolution,
        'Queue Name': queue,
        'Region': region,
        'Market': market,
        'Creation Time': creation_time,
        'Last Update Time': last_update_time,
        'Resolution time': resolution_time_days
    })

# Create DataFrame
df = pd.DataFrame(data)

# Create some intentional misclassifications
# High severity with Minor priority
high_minor = df[(df['Severity'].str.contains('High')) & (df['Priority'] == 'Minor')].index
if len(high_minor) > 0:
    sample_size = min(50, len(high_minor))
    misclass_1 = np.random.choice(high_minor, size=sample_size, replace=False)

# Medium severity with Critical priority
med_critical = df[(df['Severity'].str.contains('Medium')) & (df['Priority'] == 'Critical')].index
if len(med_critical) > 0:
    sample_size = min(80, len(med_critical))
    misclass_2 = np.random.choice(med_critical, size=sample_size, replace=False)

print("=" * 70)
print("SYNTHETIC SUPPORT CASE DATA GENERATED SUCCESSFULLY")
print("=" * 70)

print(f"\n DATASET SUMMARY")
print(f"Total Cases: {len(df):,}")
print(f"Date Range: {df['Creation Time'].min()} to {df['Creation Time'].max()}")

print(f"\n REGIONAL DISTRIBUTION")
print(df['Region'].value_counts())

print(f"\n PRIORITY DISTRIBUTION")
print(df['Priority'].value_counts())

print(f"\n AVERAGE RESOLUTION TIME BY REGION (days)")
regional_avg = df.groupby('Region')['Resolution time'].mean().round(1)
for region, avg_time in regional_avg.items():
    print(f"  {region}: {avg_time} days")

print(f"\n TOP 5 MOST COMMON ISSUES")
print(df['Reported Issue'].value_counts().head())

print(f"\n CASE STATUS BREAKDOWN")
print(df['Case status'].value_counts())

# Save to CSV
output_path = 'data/synthetic_case_data.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)
print(f"\n Data saved to: {output_path}")

# Display sample records
print(f"\n SAMPLE RECORDS (First 5):")
print(df.head().to_string())

# Summary statistics
print(f"\n DETAILED STATISTICS BY REGION AND PRIORITY:")
summary = df.groupby(['Region', 'Priority'])['Resolution time'].agg(['mean', 'median', 'std', 'count']).round(1)
print(summary)
