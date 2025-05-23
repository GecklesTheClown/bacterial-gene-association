from spmf import Spmf
import pandas as pd

def convert(df, use_names=False):
    with open('transactions.txt', 'w') as f:
        for _, row in df.iterrows():
            if use_names:
                items = [str(col) for col in df.columns if row[col] == 1]
            else:
                items = [str(i+1) for i, val in enumerate(row) if val == 1]
            f.write(" ".join(items) + "\n")
def main():
    
    df = pd.read_csv('data/DRX100168.csv').drop('FILE', axis=1)
    convert(df)
        
    spmf = Spmf("NegFIN",
                input_filename="transactions.txt",
                output_filename="output.txt",
                arguments=[0.8],
                spmf_bin_location_dir="./")  # ← ✔ points to directory containing spmf.jar

    spmf.run()   
    
    

if __name__ == "__main__":
    main()
