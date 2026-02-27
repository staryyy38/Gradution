import pandas as pd
import os
import sys

def check_new_data():
    base_dir = r"c:\Users\stars\Desktop\客户数据部分实验\Order Picking Dataset from a Warehouse of a Footwear Manufacturing Company"
    
    print("Loading files...")
    df_waves = pd.read_csv(os.path.join(base_dir, "Picking_Wave.csv"), sep=';')
    df_locs = pd.read_csv(os.path.join(base_dir, "Storage_Location.csv"), sep=',')
    
    # Clean
    df_waves['locations'] = df_waves['locations'].astype(str).str.strip()
    df_locs['originalLocation'] = df_locs['originalLocation'].astype(str).str.strip()
    
    # Merge
    print("Merging...")
    df_merged = pd.merge(df_waves, df_locs[['originalLocation', 'z']], left_on='locations', right_on='originalLocation', how='left')
    
    print("Z Distribution in Picking Wave (Lines):")
    print(df_merged['z'].value_counts(dropna=False))
    print(df_merged['z'].value_counts(normalize=True, dropna=False))
    
    # Check High Z
    high_z = df_merged[df_merged['z'] >= 3]
    print(f"Total High Z (>=3) lines: {len(high_z)}")

if __name__ == "__main__":
    check_new_data()
