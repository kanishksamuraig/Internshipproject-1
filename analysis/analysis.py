import subprocess
import pandas as pd

def parse_protocol_hierarchy(output):
    data = []
    lines = output.splitlines()
    
    for line in lines:
        if "frames:" in line and "bytes:" in line:
            parts = line.split()
            protocol = parts[0]
            frames = int(parts[1].split(':')[1])
            bytes_ = int(parts[2].split(':')[1])
            level = line.index(protocol) // 2
            data.append((protocol, frames, bytes_, level))
    
    return data

def get_protocol_hierarchy(pcap_file):
    command = ["tshark", "-r", pcap_file, "-q", "-z", "io,phs"]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout
        parsed_data = parse_protocol_hierarchy(output)
        df = pd.DataFrame(parsed_data, columns=["Protocol", "Frames", "Bytes", "Level"])
        return df
    except subprocess.CalledProcessError as e:
        print(f"Error running tshark: {e}")
        return None

def extract_hierarchy_info(pcap_file):
    protocol_hierarchy_df = get_protocol_hierarchy(pcap_file)
    
    if protocol_hierarchy_df is not None:
        level_2_df = protocol_hierarchy_df[protocol_hierarchy_df['Level'] == 2]
        level_3_df = protocol_hierarchy_df[protocol_hierarchy_df['Level'] == 3]
        
        ipv4_present = 'ip' in level_2_df['Protocol'].values
        ipv6_present = 'ipv6' in level_2_df['Protocol'].values
        
        hierarchy_info = {
            "IPv4_Present": ipv4_present,
            "IPv6_Present": ipv6_present,
            "Level_2": level_2_df.to_dict(orient='records'),
            "Level_3": level_3_df.to_dict(orient='records')
        }
        
        return hierarchy_info
    else:
        return {}
