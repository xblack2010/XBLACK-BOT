import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp , random
from protobuf_decoder.protobuf_decoder import Parser

from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import byte
import asyncio
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time
import urllib3
from important_zitado import*
from byte import*
tempid = None
sent_inv = False
start_par = False
pleaseaccept = False
nameinv = "none"
idinv = 0
senthi = False
statusinfo = False
tempdata1 = None
tempdata = None
leaveee = False
leaveee1 = False
data22 = None
isroom = False
isroom2 = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import socket

# VariabLes dyli 
#------------------------------------------#
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
evo_cycle_running = False
evo_cycle_task = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
clan_id_global = None
#------------------------------------------#

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB53"}
BADGE_VALUES = {
    "s1": 1048576,
    "s2": 32768,
    "s3": 2048,
    "s4": 64,
    "s5": 262144
}
# ---- Emote IDs Dictionary ----
EMOTE_LIST = {

   'e1': {'name': 'EVO UMP', 'id': 909000098, 'teamcode': '[FFFFFF]/e1 [FFFF00]TEAMCODE'},

    'e2': {'name': 'EVO AK47', 'id': 909000063, 'teamcode': '[FFFFFF]/e2 [FFFF00]TEAMCODE'},

    'e3': {'name': 'EVO MP40', 'id': 909000075, 'teamcode': '[FFFFFF]/e3 [FFFF00]TEAMCODE'},

    'e4': {'name': 'EVO M10', 'id': 909000081, 'teamcode': '[FFFFFF]/e4 [FFFF00]TEAMCODE'},

    'e5': {'name': 'EVO SCAR', 'id': 909000068, 'teamcode': '[FFFFFF]/e5 [FFFF00]TEAMCODE'},

    'e6': {'name': 'EVO XM8', 'id':909000085, 'teamcode': '[FFFFFF]/e6 [FFFF00]TEAMCODE'},

    'e7': {'name': 'EVO P90', 'id': 909049010, 'teamcode': '[FFFFFF]/e7 [FFFF00]TEAMCODE'},

    'e8': {'name': 'EVO FAMASH', 'id': 909000090, 'teamcode': '[FFFFFF]/e8 [FFFF00]TEAMCODE'},

    'e9': {'name': 'EVO MP40 2', 'id': 909040010, 'teamcode': '[FFFFFF]/e9 [FFFF00]TEAMCODE'},

    'e10': {'name': 'EVO PARAFAL', 'id': 909045001, 'teamcode': '[FFFFFF]/e10 [FFFF00]TEAMCODE'},

    'e11': {'name': 'EVO M1887', 'id': 909035007, 'teamcode': '[FFFFFF]/e11 [FFFF00]TEAMCODE'},

    'e12': {'name': 'EAGLE REAR', 'id': 909047004, 'teamcode': '[FFFFFF]/e12 [FFFF00]TEAMCODE'},

    'e13': {'name': '100 LEVEL', 'id': 909042007, 'teamcode': '[FFFFFF]/e13 [FFFF00]TEAMCODE'},

    'e14': {'name': 'GHOST', 'id': 909036001, 'teamcode': '[FFFFFF]/e14 [FFFF00]TEAMCODE'},

    'e15': {'name': 'Free Money!', 'id': 909035001, 'teamcode': '[FFFFFF]/e15 [FFFF00]TEAMCODE'},

 

    # Add more emotes here as needed

}

EMOTE_LIST1 ={


   'e16': {'name': ' Prismatic Flight', 'id': 909051001, 'teamcode': '[FFFFFF]/e16 [FFFF00]TEAMCODE'},

    'e17': {'name': 'Gather Around', 'id':  909051002, 'teamcode': '[FFFFFF]/e17 [FFFF00]TEAMCODE'},

    'e18': {'name': 'Rain of Spikes', 'id': 909051003, 'teamcode': '[FFFFFF]/e18 [FFFF00]TEAMCODE'},

    'e19': {'name': 'Shower Time', 'id': 909051004, 'teamcode': '[FFFFFF]/e19 [FFFF00]TEAMCODE'},

    'e20': {'name': 'Celestial Shot', 'id': 909051012, 'teamcode': '[FFFFFF]/e20 [FFFF00]TEAMCODE'},

    'e21': {'name': 'On Motorbike', 'id':  909051010, 'teamcode': '[FFFFFF]/e21 [FFFF00]TEAMCODE'},

    'e22': {'name': 'Red Petals', 'id':  909051013, 'teamcode': '[FFFFFF]/e22 [FFFF00]TEAMCODE'},

    'e23': {'name': 'Puffer Ride', 'id':  909051014, 'teamcode': '[FFFFFF]/e23 [FFFF00]TEAMCODE'},

    'e24': {'name': 'Can not Stop Laughing', 'id':  909051015, 'teamcode': '[FFFFFF]/e24 [FFFF00]TEAMCODE'},

    'e25': {'name': 'Choppy Co-op', 'id':  909051017, 'teamcode': '[FFFFFF]/e25 [FFFF00]TEAMCODE'},

    'e26': {'name': 'BTS', 'id':  909050016, 'teamcode': '[FFFFFF]/e26 [FFFF00]TEAMCODE'},

    'e27': {'name': 'Rain of Spikes', 'id':  909051003, 'teamcode': '[FFFFFF]/e27 [FFFF00]TEAMCODE'},

    'e28': {'name': 'NEW LOL', 'id':  909051015, 'teamcode': '[FFFFFF]/e28 [FFFF00]TEAMCODE'},

    'e29': {'name': 'M10 2.0', 'id':  909039011, 'teamcode': '[FFFFFF]/e29 [FFFF00]TEAMCODE'},

    'e30': {'name': 'MP40 2.0', 'id':  909040010, 'teamcode': '[FFFFFF]/e30 [FFFF00]TEAMCODE'},
    # Add more emotes here as needed


}
# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

# ---- Helper Functions for New Commands ----
def fix_num(num):
    """Format numbers with separators"""
    fixed = ""
    count = 0
    num_str = str(num)
    for char in num_str:
        if char.isdigit():
            count += 1
        fixed += char
        if count == 3:
            fixed += ","
            count = 0
    return fixed
class FF_CLIENT(threading.Thread):
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.key = None
        self.iv = None
        self.get_tok()
    def connect(self, tok, host, port, packet, key, iv):
        global clients
        clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = int(port)
        clients.connect((host, port))
        clients.send(bytes.fromhex(tok))

        while True:
            data = clients.recv(9999)
            if data == b"":
                print("Connection closed by remote host")
                break

def parse_results(parsed_results):
    """Parse protobuf results into dictionary"""
    result_dict = {}
    for result in parsed_results:
        field_data = {}
        field_data["wire_type"] = result.wire_type
        if result.wire_type == "varint":
            field_data["data"] = result.data
        if result.wire_type == "string":
            field_data["data"] = result.data
        if result.wire_type == "bytes":
            field_data["data"] = result.data
        elif result.wire_type == "length_delimited":
            field_data["data"] = parse_results(result.data.results)
        result_dict[result.field] = field_data
    return result_dict
def nmnmmmmn(plain_text, key, iv):
    plain_text = bytes.fromhex(plain_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()
def join_teamcode(inv, room_id, key, iv):
    room_id_hex = ''.join(format(ord(c), 'x') for c in room_id)
    packet = f"080412b705220701090a0b1219202a07{room_id_hex}300640014ae9040a8001303946454133424438453839323231443032303331423031313131313030303230303239303030323030323530303032353442383542303530393030303033423431373232393134323230313034303631343034376462626236636163626536363734373436356530303030303066663037303930353065313262636665363810dd011abf03755154571b08004d000c0950090c560c0b0857015a0f020f5d5009085657570c0b075d0f04080809120208440b0c0000080b5101060f0f060e5c010d0d5406560c0b0b0a5b005b0d0505000d1b020a445e5b0f026270697b636b5c606d4e5e437470517d5900665b5a04010e1a094f7c575b4a5178697f480878760e50606b585259697b077e5b605c4e0d12020a446b5e08610b4f465651546b465208740a7b436940780d7d4b561d610413094f684e54574a516a75547660484172750f5a7a416547540a6c4453080f1b08084d014e4c457c41066a1649485f08490413705b7e4f7a567f5e5c590005110b455e5e79760d0a775246005f52024751745148407c096f5d69794b750e1b0a4e6c747840625c7f415e6c1d6d5f081e02007f477f7d640e7e56567e041b50575654515e1f43564a5b5c565e5d484d595e5d5854525a5c534c584c57037a015571555b545267095c6b6001017504794d6273524e765c051b0b4460037b0b4161764108487151694972606b426b75440a7c415b045205100d44540e4d6a697a4a55747c41730b6f5f487a61597d68537369745d520e1a0c4f505d037d7a7203410c77716a69536c7f755363746b667c736860600d22047c575755300b3a091d6d647370687a1d144208312e3130382e3134480350015a0c0a044944433110761a024d455a0d0a04494443321084011a024d455a0d0a044944433310d7011a024d456a02656e8201024f52"
    encrypted_packet = nmnmmmmn(packet, key, iv)
    header_length = len(encrypted_packet) // 2
    print(f" goo > {header_length}")

    header_length_hex = dec_to_hex(header_length)
    print(f" goo > {header_length_hex}")

    if len(header_length_hex) == 2:
        final_packet = "0515000000" + header_length_hex + encrypted_packet
    elif len(header_length_hex) == 3:
        final_packet = "051500000" + header_length_hex + encrypted_packet
    elif len(header_length_hex) == 4:
        final_packet = "05150000" + header_length_hex + encrypted_packet
    elif len(header_length_hex) == 5:
        final_packet = "05150000" + header_length_hex + encrypted_packet
    else:
        raise ValueError("eororr 505 🐜")

    inv.send(bytes.fromhex(final_packet))

def get_available_room(input_text):
    """Parse protobuf packet data"""
    try:
        parsed_results = Parser().parse(input_text)
        parsed_results_objects = parsed_results
        parsed_results_dict = parse_results(parsed_results_objects)
        json_data = json.dumps(parsed_results_dict)
        return json_data
    except Exception as e:
        print(f"error {e}")
        return None
evo_emotes = {
    "1": "909000063",   # AK
    "2": "909000068",   # SCAR
    "3": "909000075",   # 1st MP40
    "4": "909040010",   # 2nd MP40
    "5": "909000081",   # 1st M1014
    "6": "909039011",   # 2nd M1014
    "7": "909000085",   # XM8
    "8": "909000090",   # Famas
    "9": "909000098",   # UMP
    "10": "909035007",  # M1887
    "11": "909042008",  # Woodpecker
    "12": "909041005",  # Groza
    "13": "909033001",  # M4A1
    "14": "909038010",  # Thompson
    "15": "909038012",  # G18
    "16": "909045001",  # Parafal
    "17": "909049010",  # P90
    "18": "909051003"   # m60
}
def get_server_info(uid):
    """Get server name and region from ban API"""
    try:
        url = f"https://ban-info-watashii.vercel.app/ban-info?uid={uid}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            region = data.get('region', 'bd').lower()
            
            server_mapping = {
                'bd': 'bd',
                'ind': 'ind', 
                'br': 'br',
                'us': 'us',
                'sac': 'sac',
                'na': 'na',
                'me': 'me',
                'sg': 'sg'
            }
            
            server_name = server_mapping.get(region, 'bd')
            
            return {
                'server_name': server_name,
                'region': region,
                'status': 'success',
                'nickname': data.get('nickname', 'Unknown'),
                'ban_status': data.get('ban_status', 'Unknown')
            }
        else:
            return {
                'server_name': 'bd',
                'region': 'bd',
                'status': 'fallback'
            }
    except Exception as e:
        print(f"Error getting server info: {e}")
        return {
            'server_name': 'bd',
            'region': 'bd',
            'status': 'error'
        }
async def evo_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG):
    """Cycle through all evolution emotes - BOT DOES OPPOSITE"""
    global evo_cycle_running
    
    # GET BOT UID FROM LOGIN DATA
    try:
        bot_uid = LoGinDaTaUncRypTinG.AccountUID
        print(f"🤖 Using bot UID from login: {bot_uid}")
    except:
        bot_uid = 13743555551
        print(f"🤖 Using hardcoded bot UID: {bot_uid}")
    
    cycle_count = 0
    while evo_cycle_running:
        cycle_count += 1
        print(f"Starting evolution emote cycle #{cycle_count}")
        
        emote_list = list(evo_emotes.items())
        total_emotes = len(emote_list)
        
        for index, (emote_number, emote_id) in enumerate(emote_list):
            if not evo_cycle_running:
                break
                
            # USER does emote #X
            for uid in uids:
                try:
                    uid_int = int(uid)
                    user_emote = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', user_emote)
                    print(f"👤 User emote #{emote_number}")
                except Exception as e:
                    print(f"Error: {e}")
            
            await asyncio.sleep(0.5)
            
            # BOT does opposite emote
            opposite_index = total_emotes - 1 - index
            opposite_number, opposite_id = emote_list[opposite_index]
            
            try:
                bot_self_emote = await Emote_k(int(bot_uid), int(opposite_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
                
                await asyncio.sleep(0.3)
                if uids:
                    first_uid = int(uids[0])
                    bot_to_user = await Emote_k(first_uid, int(opposite_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_to_user)
                
                print(f"🤖 Bot OPPOSITE emote #{opposite_number}")
            except Exception as e:
                print(f"Bot error: {e}")
            
            # Wait 5 seconds before next emote
            if evo_cycle_running:
                wait_time = 5
                for i in range(wait_time):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
    
    print("Cycle stopped")
async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3, region='BD'):
    """Safely send message with retry mechanism"""
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
            print(f"Message sent successfully on attempt {attempt + 1}")
            return True
        except Exception as e:
            print(f"Failed to send message (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)  # Wait before retry
    return False    
async def handle_badge_command(cmd, inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle individual badge commands"""
    parts = inPuTMsG.strip().split()
    if len(parts) < 2:
        error_msg = f"[b][c][FF0000]❌ Usage: /{cmd} (uid)\nExample: /{cmd} 123456789\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    badge_value = BADGE_VALUES.get(cmd, 1048576)
    
    if not target_uid.isdigit():
        error_msg = f"[b][c][FF0000]❌ Please write a valid player ID!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"[b][c][1E90FF]🌀 Request received! Preparing to spam {target_uid}...\n"
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        # Reset bot state
        await reset_bot_state(key, iv, region)
        
        # Create and send join packets
        join_packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
        spam_count = 5
        
        for i in range(spam_count):
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            print(f"✅ Sent /{cmd} request #{i+1} with badge {badge_value}")
            await asyncio.sleep(0.1)
        
        success_msg = f"[b][c][00FF00]✅ Successfully Sent {spam_count} Join Requests!\n🎯 Target: {target_uid}\n🏷️ Badge: {badge_value}\n"
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Cleanup
        await asyncio.sleep(1)
        await reset_bot_state(key, iv, region)
        
    except Exception as e:
        error_msg = f"[b][c][FF0000]❌ Error in /{cmd}: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
async def leave_squad(key, iv, region):
    """Leave squad - converted from your old TCP leave_s()"""
    fields = {
        1: 7,
        2: {
            1: 12480598706  # Your exact value from old TCP
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)         
async def reset_bot_state(key, iv, region):
    """Reset bot to solo mode before spam - Critical step from your old TCP"""
    try:
        # Leave any current squad (using your exact leave_s function)
        leave_packet = await leave_squad(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.5)
        
        print("✅ Bot state reset - left squad")
        return True
        
    except Exception as e:
        print(f"❌ Error resetting bot: {e}")
        return False

async def request_join_with_badge(target_uid, badge_value, key, iv, region):
    """Send join request with specific badge - converted from your old TCP"""
    fields = {
        1: 33,
        2: {
            1: int(target_uid),
            2: region.upper(),
            3: 1,
            4: 1,
            5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
            6: "iG:[c][b][FF0000]Watashii",
            7: 330,
            8: 1000,
            10: region.upper(),
            11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                       97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
            12: 1,
            13: int(target_uid),
            14: {
                1: 2203434355,
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            16: 1,
            17: 1,
            18: 312,
            19: 46,
            23: bytes([16, 1, 24, 1]),
            24: int(await xBunnEr()),
            26: "",
            28: "",
            31: {
                1: 1,
                2: badge_value  # Dynamic badge value
            },
            32: badge_value,    # Dynamic badge value
            34: {
                1: int(target_uid),
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        },
        10: "en",
        13: {
            2: 1,
            3: 1
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)

# ASYNC VERSION of newinfo
async def newinfo_async(uid):
    """Get player info using info-murex.vercel.app API - ASYNC VERSION"""
    try:
        url = f"https://xfaraz/info?uid={uid}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ [NEWINFO-ASYNC] Response: {data}")

                    # Check for basicinfo
                    if "basicinfo" in data and isinstance(data["basicinfo"], list) and len(data["basicinfo"]) > 0:
                        data["basic_info"] = data["basicinfo"][0]
                    else:
                        print("❌ [NEWINFO-ASYNC] 'basicinfo' not found")
                        return {"status": "wrong_id"}

                    # Check for claninfo
                    if "claninfo" in data and isinstance(data["claninfo"], list) and len(data["claninfo"]) > 0:
                        data["clan_info"] = data["claninfo"][0]
                    else:
                        data["clan_info"] = "false"

                    # Check for clanadmin
                    if "clanadmin" in data and isinstance(data["clanadmin"], list) and len(data["clanadmin"]) > 0:
                        data["clan_admin"] = data["clanadmin"][0]
                    else:
                        data["clan_admin"] = "false"

                    return {"status": "ok", "info": data}

                elif response.status == 500:
                    print("❌ [NEWINFO-ASYNC] Server Error: 500, using fallback bd")
                    # Fallback to bd region when server error
                    return {
                        "status": "ok",
                        "info": {
                            "basic_info": {
                                "nickname": "Unknown",
                                "region": "bd"
                            },
                            "clan_info": "false",
                            "clan_admin": "false"
                        }
                    }

                print(f"❌ [NEWINFO-ASYNC] Status: {response.status}")
                return {"status": "wrong_id"}

    except Exception as e:
        print(f"❌ [NEWINFO-ASYNC] Error: {str(e)}, using fallback bd")
        # Fallback to bd region on any exception
        return {
            "status": "ok",
            "info": {
                "basic_info": {
                    "nickname": "Unknown",
                    "region": "bd"
                },
                "clan_info": "false",
                "clan_admin": "false"
            }
        }

# NEW INFO FUNCTION using the new API
async def check_player_info(uid):
    """Get comprehensive player info from API - ASYNC VERSION"""
    # First try to get region from ban API
    ban_info = await check_banned_status(uid)
    
    # Fallback to old method if ban API fails
    if 'error' in ban_info or not ban_info.get('player_info'):
        print(f"[INFO] Ban API failed, using fallback get_server_info for region")
        try:
            server_info = get_server_info(uid)
            region = server_info['region']
        except Exception as e:
            print(f"[INFO] Fallback also failed: {e}, defaulting to bd")
            region = 'bd'  # Ultimate fallback
    else:
        region = ban_info['player_info'].get('region', 'bd')
    
    url = f"https://infoapiwatashii.vercel.app/info?uid={uid}&region=bd"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as response:
                if response.status == 200:
                    data = await response.json()
                    if "basicInfo" in data:
                        return {"status": "ok", "data": data}
                    else:
                        return {"status": "error", "message": data.get("error", "Invalid ID or data not found.")}
                else:
                    try:
                        error_data = await response.json()
                        error_msg = error_data.get('error', f"API returned status {response.status}")
                        return {"status": "error", "message": error_msg}
                    except:
                        return {"status": "error", "message": f"API returned status {response.status}"}

    except asyncio.TimeoutError:
        return {"status": "error", "message": "API request timed out"}
    except Exception as e:
        return {"status": "error", "message": f"Network error: {str(e)}"}
# ADDING 100 LIKES IN 24H
async def send_likes_api(uid):
    """Send likes via API - ASYNC VERSION"""
    # Get region from ban API first
    ban_info = await check_banned_status(uid)
    
    # Fallback to old method if ban API fails
    if 'error' in ban_info or not ban_info.get('player_info'):
        print(f"[LIKES] Ban API failed, using fallback get_server_info for region")
        try:
            server_info = get_server_info(uid)
            region = server_info['server_name']
        except Exception as e:
            print(f"[LIKES] Fallback also failed: {e}, defaulting to bd")
            region = 'bd'
    else:
        region = ban_info['player_info'].get('region', 'bd')
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://watashii-like.vercel.app/like?uid={uid}&server_name={region}",
                timeout=aiohttp.ClientTimeout(total=20)
            ) as likes_api_response:
                
                if likes_api_response.status == 200:
                    api_json_response = await likes_api_response.json()

                    player_name = api_json_response.get('PlayerNickname', 'Unknown')
                    likes_before = api_json_response.get('LikesbeforeCommand', 0)
                    likes_after = api_json_response.get('LikesafterCommand', 0)
                    likes_given = api_json_response.get('LikesGivenByAPI', 0)
                    status = api_json_response.get('status', 0)

                    if status == 1 and likes_given > 0:
                        return {
                            "status": "ok",
                            "message": f"""[C][B][11EAFD]‎━━━━━━━━━━━━
[FFFFFF]Likes Status:

[00FF00]Likes Sent Successfully!

[FFFFFF]Player Name : [00FF00]{player_name}  
[FFFFFF]Likes Given : [00FF00]{likes_given}  
[FFFFFF]Likes Before : [00FF00]{likes_before}  
[FFFFFF]Likes After : [00FF00]{likes_after}  
[C][B][11EAFD]‎━━━━━━━━━━━━
[C][B][FFB300]Credits: [FFFFFFXBLACKIS HERE[00FF00]!!
                """
                        }
                    elif likes_before == likes_after:
                        return {
                            "status": "failed",
                            "message": f"""[C][B][FF0000]━━━━━━━━━━━━

[FFFFFF]No Likes Sent!

[FF0000]You have already taken likes with this UID.
Try again after 24 hours.

[FFFFFF]Player Name : [FF0000]{player_name}  
[FFFFFF]Likes Before : [FF0000]{likes_before}  
[FFFFFF]Likes After : [FF0000]{likes_after}  
[C][B][FF0000]━━━━━━━━━━━━
"""
                        }
                    else:
                        return {
                            "status": "failed",
                            "message": "[C][B][FF0000]━━━━━━━━━━━━\n[FFFFFF]Unexpected Response!\nSomething went wrong.\n\nPlease try again or contact support.\n━━━━━━━━━━━━"
                        }
                else:
                    return {
                        "status": "failed",
                        "message": f"[C][B][FF0000]━━━━━\n[FFFFFF]Like API Error!\nStatus Code: {likes_api_response.status}\n━━━━━"
                    }

    except asyncio.TimeoutError:
        return {
            "status": "failed",
            "message": "[C][B][FF0000]━━━━━\n[FFFFFF]Like API Timeout!\nRequest took too long.\n━━━━━"
        }
    except Exception as e:
        return {
            "status": "failed",
            "message": f"[C][B][FF0000]━━━━━\n[FFFFFF]An unexpected error occurred:\n[FF0000]{str(e)}\n━━━━━"
        }

# CHECK ACCOUNT IS BANNED
async def check_banned_status(player_id):
    """Check if player is banned - ASYNC VERSION with NEW API STRUCTURE"""
    url = f"https://ban-info-watashii.vercel.app/ban-info?uid={player_id}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=20)) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # NEW API STRUCTURE - nested in player_info
                    player_info = data.get('player_info', {})
                    nickname = player_info.get('nickname', 'N/A')
                    region = player_info.get('region', 'N/A')
                    
                    # Ban info at root level
                    ban_status = data.get('ban_status', 'Unknown')
                    is_banned = data.get('is_banned', False)
                    ban_period = data.get('ban_period', None)
                    
                    return {
                        'status': 'BANNED' if is_banned else 'NOT BANNED',
                        'nickname': nickname,
                        'server_name': region.lower() if region != 'N/A' else 'unknown',
                        'region': region,
                        'ban_status': ban_status,
                        'ban_period': ban_period,
                        'player_info': player_info  # Keep full player_info for other functions
                    }
                else:
                    return {"error": f"Failed to fetch data. Status code: {response.status}"}
    except asyncio.TimeoutError:
        return {"error": "API request timed out"}
    except Exception as e:
        return {"error": str(e)}

# SPAM REQUESTS
async def send_spam_api(uid):
    """Send spam requests via API - ASYNC VERSION"""
    # Get region from ban API first
    ban_info = await check_banned_status(uid)
    
    # Fallback to old method if ban API fails
    if 'error' in ban_info or not ban_info.get('player_info'):
        print(f"[SPAM] Ban API failed, using fallback get_server_info for region")
        try:
            server_info = get_server_info(uid)
            region = server_info['server_name']
        except Exception as e:
            print(f"[SPAM] Fallback also failed: {e}, defaulting to bd")
            region = 'bd'
    else:
        region = ban_info['player_info'].get('region', 'bd')
    
    url = f"https://spam-api-watashii.vercel.app/send_requests?uid={uid}&server_name={region}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=20)) as res:
                if res.status == 200:
                    data = await res.json()
                    success_count = data.get('success_count', 0)
                    failed_count = data.get('failed_count', 0)
                    player_name = data.get('player_name', 'Unknown')
                    status = data.get('status', 0)
                    
                    if status == 1:
                        return {
                            "status": "ok",
                            "message": f"""[C][B][11EAFD]‎━━━━━━
[FFFFFF]Spam Request API Response:

[00FF00]Successful Requests: {success_count}

[FFFFFF]Player Name: {player_name}

[FFFFFF]Target UID: {fix_num(uid)}
[C][B][11EAFD]‎━━━━━━
[C][B][FFB300]BOT BY SIR FARAZ 
"""
                        }
                    else:
                        return {"status": "error", "message": f"API Error: Status {status}"}
                else:
                    return {"status": "error", "message": f"API Error: Status {res.status}"}
    except asyncio.TimeoutError:
        print(f"Spam API request timed out")
        return {"status": "error", "message": "Spam API request timed out."}
    except Exception as e:
        print(f"Could not connect to spam API: {e}")
        return {"status": "error", "message": str(e)}

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.123.15"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggpolarbear.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
     
async def cHTypE(H):
    if not H or H == 0: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'
    else: return 'Squid'  # Default to Squad if unknown
    
async def SEndMsG(H , message , Uid , chat_id , key , iv):

    global clan_id_global
    TypE = await cHTypE(H)
    

    if not message.startswith('['):
        message = f'[b][c]{message}'
    
    print(f'[MESSAGE_BUILD] ═══════════════════════════════════')
    print(f'[MESSAGE_BUILD] Chat Type: {TypE} (H={H})')
    print(f'[MESSAGE_BUILD] Sender UID: {Uid} | Chat ID: {chat_id}')
    print(f'[MESSAGE_BUILD] Clan ID Global: {clan_id_global}')
    print(f'[MESSAGE_BUILD] Message Preview: {message[:80]}...')
    
    if TypE == 'Squid': 

        msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
        print(f'[MESSAGE_BUILD] ✅ SQUAD packet: chat_id={chat_id}')
        
    elif TypE == 'CLan': 

        target_clan_id = clan_id_global if clan_id_global else chat_id
        msg_packet = await xSEndMsg(message , 1 , target_clan_id , chat_id , key , iv)
        print(f'[MESSAGE_BUILD] ✅ GUILD packet: Tp=1, Tp2={target_clan_id}, id={chat_id}')
        
    elif TypE == 'PrivaTe': 

        msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
        print(f'[MESSAGE_BUILD] ✅ PRIVATE packet: Tp=2, Tp2={Uid}, id={Uid}')
    
    else:
        print(f'[MESSAGE_BUILD] ❌ ERROR: Unknown chat type {H}')
        msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    
    print(f'[MESSAGE_BUILD] Packet size: {len(msg_packet)} bytes')
    print(f'[MESSAGE_BUILD] ═══════════════════════════════════')
    return msg_packet

async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):

    global whisper_writer, online_writer
    
    if not PacKeT:
        print(f'[PACKET_SEND] ❌ ERROR: Packet is None or empty!')
        return
    
    packet_size = len(PacKeT)
    packet_hex = PacKeT.hex()
    
    print(f'[PACKET_SEND] ═══════════════════════════════════')
    print(f'[PACKET_SEND] Type: {TypE} | Size: {packet_size} bytes')
    print(f'[PACKET_SEND] Hex Preview: {packet_hex[:100]}...')
    print(f'[PACKET_SEND] whisper_writer: {"✅ Connected" if whisper_writer else "❌ None"}')
    print(f'[PACKET_SEND] online_writer: {"✅ Connected" if online_writer else "❌ None"}')
    
    try:
        if TypE == 'ChaT': 

            if whisper_writer is None:
                print(f'[PACKET_SEND] ❌ CRITICAL ERROR: whisper_writer is None!')
                print(f'[PACKET_SEND] Cannot send chat message - connection lost!')
                print(f'[PACKET_SEND] ═══════════════════════════════════')
                return False
            
            whisper_writer.write(PacKeT)
            await whisper_writer.drain()
            print(f'[PACKET_SEND] ✅ Chat packet SENT to game via whisper_writer')
            print(f'[PACKET_SEND] Message should appear in game chat now!')
            print(f'[PACKET_SEND] ═══════════════════════════════════')
            return True
            
        elif TypE == 'OnLine': 

            if online_writer is None:
                print(f'[PACKET_SEND] ❌ ERROR: online_writer is None!')
                print(f'[PACKET_SEND] ═══════════════════════════════════')
                return False
            
            online_writer.write(PacKeT)
            await online_writer.drain()
            print(f'[PACKET_SEND] ✅ Online packet sent successfully')
            print(f'[PACKET_SEND] ═══════════════════════════════════')
            return True
            
        else: 
            print(f'[PACKET_SEND] ❌ ERROR: Unsupported packet type: {TypE}')
            print(f'[PACKET_SEND] Valid types: ChaT, OnLine')
            print(f'[PACKET_SEND] ═══════════════════════════════════')
            return False
            
    except Exception as e:
        print(f'[PACKET_SEND] ❌ EXCEPTION during packet send: {e}')
        print(f'[PACKET_SEND] ═══════════════════════════════════')
        return False 
           
async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer , spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2: break
                
                if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                    try:
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        packet = json.loads(packet)
                        
                        try:
                            OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)
                        except Exception as e:
                            print(f'Error parsing squad data: {e}')
                            continue

                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)
                        
                   
                        try:
                            if packet.get('5', {}).get('data', {}).get('16'):
                           
                                print('Private chat detected - sending welcome message')
                                message = f'[B][C]{get_random_color()}\n- WeLComE To Ai  Bot ! \n\n{get_random_color()}- Use /help for commands\n\n[00FF00]Dev : XBLACK'
                                P = await SEndMsG(2 , message , OwNer_UiD , OwNer_UiD , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            else:
                         
                                print('Squad chat detected - joining silently')
                        except:
                   
                            print('Joined chat/squad silently')

                    except Exception as e:
                        print(f'Error processing invite: {e}')
                        pass

            online_writer.close() ; await online_writer.wait_closed() ; online_writer = None

        except Exception as e: print(f"- ErroR With {ip}:{port} - {e}") ; online_writer = None
        await asyncio.sleep(reconnect_delay)

async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave, clan_id_global
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_id_global = clan_id  
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                    except:
                        response = None


                    if response:
                        print(f'🔥 [MESSAGE RECEIVED] ═══════════════════════════════════')
                        print(f'🔥 [MESSAGE] From UID: {uid}')
                        print(f'🔥 [MESSAGE] Chat ID: {chat_id}')
                        print(f'🔥 [MESSAGE] Chat Type: {XX}')
                        print(f'🔥 [MESSAGE] Content: "{inPuTMsG}"')
                        print(f'🔥 [MESSAGE] ═══════════════════════════════════')
                        
                

                        if inPuTMsG.startswith(("/3")):
                            print(f'[GROUP 3] Command received from UID: {uid}')
                            print(f'[GROUP 3] Chat type: {response.Data.chat_type}')
                            message = f"[B][C]{get_random_color()}\n\n✅ Creating 3-player squad...\n[FFFFFF]Accept invite fast!\n\n"
                            P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            PAc = await OpEnSq(key , iv,region)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                            C = await cHSq(3, uid ,key, iv,region)
                            await asyncio.sleep(0.5)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                            V = await SEnd_InV(3 , uid , key , iv,region)
                            await asyncio.sleep(0.5)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                            E = await ExiT(None , key , iv)
                            await asyncio.sleep(3)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                            success = f"[B][C][00FF00]\n\n✅ Squad created!\n[FFFFFF]3 players squad\n\n"
                            P2 = await SEndMsG(response.Data.chat_type , success , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P2)

                        if inPuTMsG.startswith(("/5")):
                            print(f'[GROUP 5] Command received from UID: {uid}')
                            print(f'[GROUP 5] Chat type: {response.Data.chat_type}')
                            message = f"[B][C]{get_random_color()}\n\n✅ Creating 5-player squad...\n[FFFFFF]Accept invite fast!\n\n"
                            P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            PAc = await OpEnSq(key , iv,region)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                            C = await cHSq(5, uid ,key, iv,region)
                            await asyncio.sleep(0.5)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                            V = await SEnd_InV(5 , uid , key , iv,region)
                            await asyncio.sleep(0.5)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                            E = await ExiT(None , key , iv)
                            await asyncio.sleep(3)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                            success = f"[B][C][00FF00]\n\n✅ Squad created!\n[FFFFFF]5 players squad\n\n"
                            P2 = await SEndMsG(response.Data.chat_type , success , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P2)

                        if inPuTMsG.startswith(("/6")):
                            print(f'[GROUP 6] Command received from UID: {uid}')
                            print(f'[GROUP 6] Chat type: {response.Data.chat_type}')
                            message = f"[B][C]{get_random_color()}\n\n✅ Creating 6-player squad...\n[FFFFFF]Accept invite fast!\n\n"
                            P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            PAc = await OpEnSq(key , iv,region)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                            C = await cHSq(6, uid ,key, iv,region)
                            await asyncio.sleep(0.5)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                            V = await SEnd_InV(6 , uid , key , iv,region)
                            await asyncio.sleep(0.5)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                            E = await ExiT(None , key , iv)
                            await asyncio.sleep(3)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                            success = f"[B][C][00FF00]\n\n✅ Squad created!\n[FFFFFF]6 players squad\n\n"
                            P2 = await SEndMsG(response.Data.chat_type , success , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P2)



                        if inPuTMsG.startswith('/x/'):
                            CodE = inPuTMsG.split('/x/')[1].strip()
                            print(f'[JOIN] Joining squad with code: {CodE}')
                            print(f'[JOIN] Chat type: {response.Data.chat_type}')
                            msg = f"[B][C]{get_random_color()}\n\n🎮 Joining squad...\n[FFFF00]Code: {CodE}\n\n"
                            P = await SEndMsG(response.Data.chat_type, msg, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            EM = await GenJoinSquadsPacket(CodE, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
                            await asyncio.sleep(1)
                            success = f"[B][C][00FF00]\n\n✅ Joined squad!\n[FFFFFF]Code: {CodE}\n\n"
                            P2 = await SEndMsG(response.Data.chat_type, success, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P2)

                        if inPuTMsG.startswith('/leave'):
                            print(f'[LEAVE] Leaving squad')
                            msg = f"[B][C]{get_random_color()}\n\n👋 Leaving squad...\n\n"
                            P = await SEndMsG(response.Data.chat_type, msg, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            await asyncio.sleep(0.5)
                            success = f"[B][C][00FF00]\n\n✅ Left squad!\n\n"
                            P2 = await SEndMsG(response.Data.chat_type, success, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P2)
                        
                        # /admin command - Bot admin info
                        if inPuTMsG.startswith('/admin'):
                            print(f'[ADMIN] ═══════════════════════════════════════')
                            print(f'[ADMIN] Command received from UID: {uid}')
                            
                            # Generate colors
                            c1 = get_random_color()
                            c2 = get_random_color()
                            c3 = get_random_color()
                            
                            # PART 1: Bot Info
                            admin_part1 = f"[B][C]{c1}╔══════════════════════╗\n"
                            admin_part1 += f"[FFFFFF]║ {c2}🤖 BOT ADMIN INFO [FFFFFF]║\n"
                            admin_part1 += f"{c1}╚══════════════════════╝\n\n"
                            admin_part1 += f"[FFFF00]Developer: [FFFFFF]XBLACK.\n"
                            admin_part1 += f"[FFFF00]Bot Name: [FFFFFF]Faraz Who?\n"
                            admin_part1 += f"[FFFF00]Bot UID: [FFFFFF]13650973439"
                            
                            P1 = await SEndMsG(response.Data.chat_type, admin_part1, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P1)
                            await asyncio.sleep(1.0)
                            print(f'[ADMIN] Part 1/2 sent')
                            
                            # PART 2: Contact Info
                            admin_part2 = f"[B][C]{c3}╔══════════════════════╗\n"
                            admin_part2 += f"[FFFFFF]║ {c2}📱 CONTACT INFO   [FFFFFF]║\n"
                            admin_part2 += f"{c3}╚══════════════════════╝\n\n"
                            admin_part2 += f"[FFFF00]ADMIN: [FFFFFF]XBLACK\n"
                            admin_part2 += f"[FFFF00]Status: [00FF00]Online ✅\n"
                            admin_part2 += f"[FFFF00]Type: [FFFFFF]/help for commands"
                            
                            P2 = await SEndMsG(response.Data.chat_type, admin_part2, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P2)
                            print(f'[ADMIN] Part 2/2 sent')
                            print(f'[ADMIN] ✅ ALL PARTS SENT!')
                            print(f'[ADMIN] ═══════════════════════════════════════')
                            
                        if inPuTMsG.startswith('/help'):
                            print(f'[HELP] ═══════════════════════════════════════')
                            print(f'[HELP] Command received from UID: {uid}')
                            print(f'[HELP] Chat type: {response.Data.chat_type}')
                            print(f'[HELP] Sending beautiful help menu in 5 parts...')
                            print(f'[HELP] ═══════════════════════════════════════')
                            
                            # Generate random colors for each part
                            c1 = get_random_color()
                            c2 = get_random_color()
                            c3 = get_random_color()
                            c4 = get_random_color()
                            c5 = get_random_color()
                            c6 = get_random_color()
                            c7 = get_random_color()
                            c8 = get_random_color()
                            
                            # PART 1: EMOTES - Beautiful Colorful Design
                            help_part1 = f"[B][C]{c1}╔══════════════════════╗\n"
                            help_part1 += f"[FFFFFF]║  {c2}🎭 EMOTES MENU  [FFFFFF]║\n"
                            help_part1 += f"{c1}╚══════════════════════╝\n\n"
                            help_part1 += f"{c3}┌─ List All:\n"
                            help_part1 += f"[FFFFFF]│ {c4}/emoteslist\n\n"

                            help_part1 += f"[FFFFFF]│ {c4}/emoteslist1\n\n"
                            help_part1 += f"{c6}┌─ Evo Cycle:\n"
                            help_part1 += f"[FFFFFF]│ {c3}/evos {c5}→ Start evo cycle\n"
                            help_part1 += f"[FFFFFF]│ {c3}/sevos {c5}→ Stop evo cycle\n"
                            help_part1 += f"{c3}┌─ Manual:\n"
                            help_part1 += f"[FFFFFF]│ {c4}/e [FFFF00]UID EMOTE_ID\n\n"

                            help_part1 += f"[FFFFFF]│ {c4}/admin [FFFF00]Admin Info"
                            # PART 2: GROUP MAKE - Beautiful Colorful Design
                            help_part2 = f"[B][C]{c2}╔══════════════════════╗\n"
                            help_part2 += f"[FFFFFF]║ {c6}👥 GROUP MAKER [FFFFFF]║\n"
                            help_part2 += f"{c2}╚══════════════════════╝\n\n"
                            help_part2 += f"{c7}┌─ Create Group:\n"
                            help_part2 += f"[FFFFFF]│ {c8}/3 {c5}→ Make 3 player group\n"
                            help_part2 += f"[FFFFFF]│ {c8}/5 {c5}→ Make 5 player group\n"
                            help_part2 += f"[FFFFFF]│ {c8}/6 {c5}→ Make 6 player group\n\n"
                            help_part2 += f"{c7}┌─ Invite:\n"
                            help_part2 += f"[FFFFFF]│ {c8}/inv [FFFF00]UID {c5}→ Spam invite\n"
                            help_part2 += f"[FFFFFF]│ {c8}/room [FFFF00]UID {c5}→ Room spam"
                            
                            # PART 3: BASIC COMMANDS - Beautiful Colorful Design
                            help_part3 = f"[B][C]{c3}╔══════════════════════╗\n"
                            help_part3 += f"[FFFFFF]║  {c1}🎮 BASIC MENU  [FFFFFF]║\n"
                            help_part3 += f"{c3}╚══════════════════════╝\n\n"
                            help_part3 += f"{c4}┌─ Squad Actions:\n"
                            help_part3 += f"[FFFFFF]│ {c2}/x/ [FFFF00]CODE {c5}→ Join squad\n"
                            help_part3 += f"[FFFFFF]│ {c2}/leave {c5}→ Leave squad\n"
                            #help_part3 += f"[FFFFFF]│ {c2}/s {c5}→ Ready up"
                            help_part3 += f"[FFFFFF]│ {c2}/ai {c5}→ Ai"
                            
                            # PART 4: INFO & CHECK - Beautiful Colorful Design
                            help_part4 = f"[B][C]{c4}╔══════════════════════╗\n"
                            help_part4 += f"[FFFFFF]║  {c7}ℹ️ INFO MENU   [FFFFFF]║\n"
                            help_part4 += f"{c4}╚══════════════════════╝\n\n"
                            help_part4 += f"{c6}┌─ Player Info:\n"
                            help_part4 += f"[FFFFFF]│ {c3}/info [FFFF00]UID {c5}→ Full details\n"

                            help_part4 += f"{c6}┌─ Actions:\n"
                            help_part4 += f"[FFFFFF]│ {c3}/sp/ [FFFF00]UID {c5}→ Send Join Req\n"
                            help_part4 += f"[FFFFFF]│ {c3}/spam [FFFF00]UID {c5}→ Spam req"

                            # PART 5: BADGE COMMANDS - Beautiful Colorful Design
                            help_part5 = f"[b][c]{c5}╔══════════════════════╗\n"
                            help_part5 += f"[FFFFFF]║ {c2}🏆 BADGE MENU  [FFFFFF]║\n"
                            help_part5 += f"{c5}╚══════════════════════╝\n\n"
                            help_part5 += f"{c3}┌─ Badge Spam:\n"
                            help_part5 += f"[FFFFFF]│ {c4}/s1 [FFFF00]UID {c5}→ Craftland Badge\n"
                            help_part5 += f"[FFFFFF]│ {c4}/s2 [FFFF00]UID {c5}→ New V-Badge\n"
                            help_part5 += f"[FFFFFF]│ {c4}/s3 [FFFF00]UID {c5}→ Moderator Badge\n"
                            help_part5 += f"[FFFFFF]│ {c4}/s4 [FFFF00]UID {c5}→ Small V-Badge\n"
                            help_part5 += f"[FFFFFF]│ {c4}/s5 [FFFF00]UID {c5}→ Pro Badge\n"
                            
                            # PART 6: BRUTAL ATTACKS - Beautiful Colorful Design
                            help_part6 = f"[B][C]{c5}╔══════════════════════╗\n"
                            help_part6 += f"[FFFFFF]║ {c8}⚔️ BRUTAL MODE  [FFFFFF]║\n"
                            help_part6 += f"{c5}╚══════════════════════╝\n\n"
                            help_part6 += f"{c1}┌─ Attack Modes:\n"
                            help_part6 += f"[FFFFFF]│ {c7}/attack [FFFF00]CODE\n"
                            help_part6 += f"[FFFFFF]│  {c6}→ 45s attack\n\n"
                            help_part6 += f"[FFFFFF]│ {c7}/lag [FFFF00]CODE\n"
                            help_part6 += f"[FFFFFF]│  {c6}→ Lag attack\n\n"
                            help_part6 += f"[FFFFFF]│ {c7}/start [FFFF00]CODE\n"
                            help_part6 += f"[FFFFFF]│  {c6}→ Force start\n\n"
                            help_part6 += f"{c2}╔══════════════════════╗\n"
                            help_part6 += f"[FFFFFF]║ {c4}Dev: XBLACK. [FF00FF]║\n"
                            help_part6 += f"{c2}╚══════════════════════╝"
                            
                            # Send all parts with delays
                            print(f'[HELP] Sending part 1/6: EMOTES')
                            P1 = await SEndMsG(response.Data.chat_type, help_part1, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P1)
                            await asyncio.sleep(1.0)
                            
                            print(f'[HELP] Sending part 2/6: SQUAD MAKE')
                            P2 = await SEndMsG(response.Data.chat_type, help_part2, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P2)
                            await asyncio.sleep(1.0)
                            
                            print(f'[HELP] Sending part 3/6: BASIC')
                            P3 = await SEndMsG(response.Data.chat_type, help_part3, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P3)
                            await asyncio.sleep(1.0)
                            
                            print(f'[HELP] Sending part 4/6: INFO & CHECK')
                            P4 = await SEndMsG(response.Data.chat_type, help_part4, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P4)
                            await asyncio.sleep(1.0)
                            
                            print(f'[HELP] Sending part 5/6: BRUTAL ATTACKS')
                            P5 = await SEndMsG(response.Data.chat_type, help_part5, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P5)

                            P6 = await SEndMsG(response.Data.chat_type, help_part6, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P6)
                            await asyncio.sleep(1.0)
                            
                            print(f'[HELP] ✅ ALL 6 BEAUTIFUL COLORFUL PARTS SENT!')
                            print(f'[HELP] ═══════════════════════════════════════')

                        if inPuTMsG.startswith('/emoteslist'):
                            print(f'[EMOTESLIST] Command received from UID: {uid}')
                            print(f'[EMOTESLIST] Chat type: {response.Data.chat_type}')
                            emote_list_msg = f"[B][C]{get_random_color()}\n\n📋 Available Emotes:\n\n"
                            for emote_key, emote_value in EMOTE_LIST.items():
                                emote_list_msg += f"{emote_value['teamcode']} - [00FF00]{emote_value['name']}\n"
                            emote_list_msg += f"\n[FFFF00]Example: /e1 123345\n"
                            
                            P = await SEndMsG(response.Data.chat_type, emote_list_msg, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            print(f'[EMOTESLIST] Message sent successfully')

                        # Handle quick emote commands (/e1, /e2, /hh, etc.)
                        for emote_cmd, emote_data in EMOTE_LIST.items():
                            if inPuTMsG.strip().startswith(f'/{emote_cmd} '):
                                print(f'[{emote_cmd.upper()}] Quick emote detected from UID: {uid}')
                                print(f'[{emote_cmd.upper()}] Chat type: {response.Data.chat_type}')
                                
                                # Extract sender name from protobuf
                                sender_name = response.Data.Details.Nickname if response.Data.Details else 'Unknown'
                                
                                parts = inPuTMsG.strip().split()
                                if len(parts) < 2:
                                    print(f'[{emote_cmd.upper()}] ERROR: Missing team code')
                                    error_msg = f"[B][C]{get_random_color()}\n\n❌ Invalid format!\n\n[FFFFFF]Use: /{emote_cmd} [FFFF00]TEAMCODE\n[FFFFFF]Example: /{emote_cmd} [FFFF00]123454\n"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                else:
                                    team_code = parts[1].upper()
                                    emote_id = emote_data['id']
                                    emote_name = emote_data['name']
                                    
                                    print(f'[{emote_cmd.upper()}] Sender Name: {sender_name}')
                                    print(f'[{emote_cmd.upper()}] Sender UID: {uid}')
                                    print(f'[{emote_cmd.upper()}] Team Code: {team_code}')
                                    print(f'[{emote_cmd.upper()}] Emote ID: {emote_id}')
                                    print(f'[{emote_cmd.upper()}] Emote Name: {emote_name}')
                                    
                                    try:
                                        # STEP 1: Join squad - ULTRA FAST
                                        print(f'[{emote_cmd.upper()}] STEP 1: Joining squad {team_code}...')
                                        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                        await asyncio.sleep(0.15)  # Ultra fast - 150ms
                                        print(f'[{emote_cmd.upper()}] Squad joined!')
                                        
                                        # STEP 2: Send emote - ULTRA FAST
                                        print(f'[{emote_cmd.upper()}] STEP 2: Sending emote to UID {uid}...')
                                        emote_packet = await Emote_k(uid, emote_id, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
                                        await asyncio.sleep(0.1)  # Ultra fast - 100ms
                                        print(f'[{emote_cmd.upper()}] Emote sent!')
                                        
                                        # STEP 3: Leave squad - INSTANT
                                        print(f'[{emote_cmd.upper()}] STEP 3: Leaving squad...')
                                        leave_packet = await ExiT(None, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
                                        print(f'[{emote_cmd.upper()}] Squad left!')
                                        
                                        # Send success message with sender name
                                        success_msg = f"[B][C]{get_random_color()}\n\n✅ Success!\n[00FF00]{emote_name} [FFFFFF]sent to [FFFF00]{sender_name}[FFFFFF]!\n"
                                        P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        print(f'[{emote_cmd.upper()}] SUCCESS: Emote process completed in 0.25s!')
                                        
                                    except Exception as e:
                                        print(f'[{emote_cmd.upper()}] ERROR: {e}')
                                        error_msg = f"[B][C]{get_random_color()}\n\n❌ Failed!\n[FFFFFF]Error: {str(e)}\n"
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                
                                break  # Exit loop after handling


                        if inPuTMsG.startswith('/emoteslist1'):
                            try:
                                dd = chatdata['5']['data']['16']
                                print(f'[EMOTESLIST1] Command received from UID: {uid}')
                                emote_list_msg1 = f"[B][C]{get_random_color()}\n\n📋 Available Emotes:\n\n"
                                for emote_key, emote_value in EMOTE_LIST1.items():
                                    emote_list_msg1 += f"{emote_value['teamcode']} - [00FF00]{emote_value['name']}\n"
                                emote_list_msg1 += f"\n[FFFF00]Example: /e1 ABC123\n"
                                
                                P = await SEndMsG(response.Data.chat_type, emote_list_msg1, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                print(f'[EMOTESLIST1] Message sent successfully')
                            except KeyError:
                                print(f'[EMOTESLIST1] Ignored in squad chat')
                                pass

                         # Handle quick emote commands (/e1, /e2, /hh, etc.)

                        for emote_cmd, emote_data in EMOTE_LIST1.items():
                            if inPuTMsG.strip().startswith(f'/{emote_cmd} '):
                                try:
                                    dd = chatdata['5']['data']['16']
                                    print(f'[{emote_cmd.upper()}] Quick emote detected from UID: {uid}')
                                    
                                    # Extract sender name from protobuf
                                    sender_name = response.Data.Details.Nickname if response.Data.Details else 'Unknown'
                                    
                                    parts = inPuTMsG.strip().split()
                                    if len(parts) < 2:
                                        print(f'[{emote_cmd.upper()}] ERROR: Missing team code')
                                        error_msg = f"[B][C]{get_random_color()}\n\n❌ Invalid format!\n\n[FFFFFF]Use: /{emote_cmd} [FFFF00]TEAMCODE\n[FFFFFF]Example: /{emote_cmd} [FFFF00]ABC123\n"
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        break
                                    
                                    team_code = parts[1].upper()
                                    emote_id = emote_data['id']
                                    emote_name = emote_data['name']
                                    
                                    print(f'[{emote_cmd.upper()}] Sender Name: {sender_name}')
                                    print(f'[{emote_cmd.upper()}] Sender UID: {uid}')
                                    print(f'[{emote_cmd.upper()}] Team Code: {team_code}')
                                    print(f'[{emote_cmd.upper()}] Emote ID: {emote_id}')
                                    print(f'[{emote_cmd.upper()}] Emote Name: {emote_name}')
                                    
                                    try:
                                        # STEP 1: Join squad - ULTRA FAST
                                        print(f'[{emote_cmd.upper()}] STEP 1: Joining squad {team_code}...')
                                        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                        await asyncio.sleep(0.15)  # Ultra fast - 150ms
                                        print(f'[{emote_cmd.upper()}] Squad joined!')
                                        
                                        # STEP 2: Send emote - ULTRA FAST
                                        print(f'[{emote_cmd.upper()}] STEP 2: Sending emote to UID {uid}...')
                                        emote_packet = await Emote_k(uid, emote_id, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
                                        await asyncio.sleep(0.1)  # Ultra fast - 100ms
                                        print(f'[{emote_cmd.upper()}] Emote sent!')
                                        
                                        # STEP 3: Leave squad - INSTANT
                                        print(f'[{emote_cmd.upper()}] STEP 3: Leaving squad...')
                                        leave_packet = await ExiT(None, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
                                        print(f'[{emote_cmd.upper()}] Squad left!')
                                        
                                        # Send success message with sender name
                                        success_msg = f"[B][C]{get_random_color()}\n\n✅ Success!\n[00FF00]{emote_name} [FFFFFF]sent to [FFFF00]{sender_name}[FFFFFF]!\n"
                                        P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        print(f'[{emote_cmd.upper()}] SUCCESS: Emote process completed in 0.25s!')
                                        
                                    except Exception as e:
                                        print(f'[{emote_cmd.upper()}] ERROR: {e}')
                                        error_msg = f"[B][C]{get_random_color()}\n\n❌ Failed!\n[FFFFFF]Error: {str(e)}\n"
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    
                                    break  # Exit loop after handling
                                    
                                except KeyError:
                                    print(f'[{emote_cmd.upper()}] Ignored in squad chat')
                                    break                               

                        # Manual emote command
                        if inPuTMsG.strip().startswith('/e '):
                            print(f'[MANUAL EMOTE] Command received from UID: {uid}')
                            print(f'[MANUAL EMOTE] Chat type: {response.Data.chat_type}')
                            
                            parts = inPuTMsG.strip().split()
                            print(response.Data.chat_type, uid, chat_id)
                            
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]Usage: /e UID [UID2] [UID3] [UID4] [UID5] EMOTE_ID\n[FFFFFF]Example: /e 123456789 909000098\n[FFFF00]Max 5 targets"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            else:
                                target_uid = uid2 = uid3 = uid4 = uid5 = None
                                s = False

                                try:
                                    target_uid = int(parts[1])
                                    if len(parts) > 2: uid2 = int(parts[2]) if len(parts) == 3 else None
                                    if len(parts) > 3: uid3 = int(parts[3]) if len(parts) > 3 else None
                                    if len(parts) > 4: uid4 = int(parts[4]) if len(parts) > 4 else None
                                    if len(parts) > 5: uid5 = int(parts[5]) if len(parts) > 5 else None
                                    idT = int(parts[-1])  # Emote ID is always the last parameter

                                except ValueError as ve:
                                    print("ValueError:", ve)
                                    s = True
                                    error_msg = f"[B][C][FF0000]❌ Invalid UID or Emote ID!\n[FFFFFF]Make sure all UIDs and Emote ID are numbers."
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                                except Exception as e:
                                    print(f"Exception parsing manual emote: {e}")
                                    s = True
                                    error_msg = f"[B][C][FF0000]❌ Error parsing command!"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                                if not s and target_uid:
                                    try:
                                        # Count total targets
                                        targets = [target_uid]
                                        if uid2: targets.append(uid2)
                                        if uid3: targets.append(uid3)
                                        if uid4: targets.append(uid4)
                                        if uid5: targets.append(uid5)
                                        
                                        message = f'[B][C]{get_random_color()}\n✨ Sending Emote ID: {idT}\n[FFFFFF]To {len(targets)} target(s)...\n'
                                        P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                                        # Send emotes to all targets
                                        H = await Emote_k(target_uid, idT, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)

                                        if uid2:
                                            H = await Emote_k(uid2, idT, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid3:
                                            H = await Emote_k(uid3, idT, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid4:
                                            H = await Emote_k(uid4, idT, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid5:
                                            H = await Emote_k(uid5, idT, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)

                                        # Success message
                                        success_msg = f'[B][C][00FF00]\n✅ Emote sent successfully!\n[FFFFFF]Emote ID: [00FF00]{idT}\n[FFFFFF]Targets: [00FF00]{len(targets)}'
                                        P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        print(f'[MANUAL EMOTE] Success: Emote {idT} sent to {len(targets)} targets')

                                    except Exception as e:
                                        print(f"Error sending manual emote: {e}")
                                        error_msg = f'[B][C][FF0000]\n❌ Failed to send emote!\n[FFFFFF]Error: {str(e)}'
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                        # ========== NEW COMMANDS FROM WATASHII ==========



                        if inPuTMsG.startswith('/sp/'):
                            CodE = inPuTMsG.split('/sp/')[1]
                            try:
                                dd = chatdata['5']['data']['16']


                                async def squad_invite_cycle():
                                    try:
                                        PAc = await OpEnSq(key , iv, region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(3, CodE ,key, iv, region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv, region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                        await asyncio.sleep(0.001)

                                        PAc = await OpEnSq(key , iv, region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(5, CodE ,key, iv, region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv, region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                        await asyncio.sleep(0.001)

                                        PAc = await OpEnSq(key , iv, region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(6, CodE ,key, iv, region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv, region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                    except Exception as e:
                                        print(f"Error inside squad_invite_cycle: {e}")

                                # Create tasks instead of using threads for async functions
                                invite_tasks = []
                                for _ in range(25): # Increased from 1 to 25 for effective spamming
                                    task = asyncio.create_task(squad_invite_cycle())
                                    invite_tasks.append(task)
                                    await asyncio.sleep(0.2) # Stagger tasks to avoid overwhelming the server

                                # Wait for all tasks to complete
                                await asyncio.gather(*invite_tasks, return_exceptions=True)
                            except:
                                print('msg in squad')
                        # /likes command - Send likes (FIXED - Added debugging and success message)
                        if inPuTMsG.startswith('/like'):
                                target_uid = None  # Initialize at start
                                print(f'[LIKES] ═══════════════════════════════════════')
                                print(f'[LIKES] Command received from UID: {uid}')
                                print(f'[LIKES] Chat type: {response.Data.chat_type}')
                                print(f'[LIKES] Chat ID: {chat_id}')
                                parts = inPuTMsG.strip().split()
                                
                                if len(parts) < 2:
                                    error_msg = f"[B][C][FF0000]❌ Usage: /likes UID\n[FFFFFF]Example: /likes 12345678"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                else:
                                    target_uid = parts[1]
                                    print(f'[LIKES] Target UID: {target_uid}')
                                    
                                    # Send loading message 
                                    loading_msg = f"[B][C][11EAFD]⏳ Sending likes to {fix_num(target_uid)}..."
                                    P = await SEndMsG(response.Data.chat_type, loading_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    await asyncio.sleep(1.0)  # INCREASED DELAY LIKE /help
                                    print(f'[LIKES] Loading message sent, calling API...')
                                    
                                    try:
                                        # Call API and get formatted response 
                                        likes_response = await send_likes_api(target_uid)
                                        print(f'[LIKES] API Response: {likes_response}')
                                        
                                        # Send the complete formatted message from API
                                        await asyncio.sleep(1.0)  # CRITICAL DELAY LIKE /help
                                        P = await SEndMsG(response.Data.chat_type, likes_response['message'], uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        print(f'[LIKES] ✅ SUCCESS: Response sent for {target_uid}')
                                        
                                        # Add success confirmation message
                                        await asyncio.sleep(1.0)
                                        success_msg = f"[B][C][00FF00]✅ Likes sent successfully to {fix_num(target_uid)}!"
                                        P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        print(f'[LIKES] ✅ SUCCESS: Confirmation sent')
                                        
                                    except Exception as e:
                                        print(f'[LIKES] ❌ EXCEPTION: {e}')
                                        await asyncio.sleep(1.0)
                                        error_msg = f"[B][C][FF0000]❌ Failed to send likes: Undermaintenance."
                                        # error_msg = f"[B][C][FF0000]❌ Failed to send likes: {str(e)}"
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    
                                    print(f'[LIKES] ═══════════════════════════════════════')

                        # /check command - Check ban status (SPLIT MESSAGES - BYTE DETECTION)
                        if "1200" in data.hex()[0:4] and b"/check" in data:
                            try:
                                print('🔥 [CHECK] Command detected')
                                command_split = re.split(b"/check", data)
                                
                                if len(command_split) <= 1:
                                    error_msg = "[B][C][FF0000]❌ Usage: /check UID"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                else:
                                    # Extract UID
                                    command_str = command_split[1].decode('utf-8', errors='ignore')
                                    uids = re.findall(r"\b\d{5,15}\b", command_str)
                                    target_uid = uids[0] if uids else ""
                                    
                                    if not target_uid:
                                        error_msg = "[B][C][FF0000]❌ Invalid ID"
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    else:
                                        print(f'🔥 [CHECK] Target: {target_uid}')
                                        
                                        # Loading
                                        loading_msg = "[B][C][FFFF00]⏳ Checking..."
                                        P = await SEndMsG(response.Data.chat_type, loading_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        await asyncio.sleep(1.0)
                                        
                                        try:
                                            banned_response = await check_banned_status(target_uid)
                                            print(f'🔥 [CHECK] API Response: {banned_response}')
                                            
                                            if 'error' in banned_response:
                                                error_msg = "[B][C][FF0000]❌ API Error"
                                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                            else:
                                                player_info = banned_response.get('player_info', {})
                                                name = player_info.get('nickname', 'Unknown')[:15]  # Limit name
                                                region = player_info.get('region', 'N/A')
                                                ban_status = banned_response.get('ban_status', 'Unknown')
                                                is_banned = banned_response.get('is_banned', False)
                                                
                                                # Part 1: Status
                                                if is_banned:
                                                    msg1 = f"[B][C][FF0000]⚠️ BANNED\n[FFFFFF]Player: {name}"
                                                else:
                                                    msg1 = f"[B][C][00FF00]✅ NOT BANNED\n[FFFFFF]Player: {name}"
                                                
                                                await asyncio.sleep(1.0)
                                                P = await SEndMsG(response.Data.chat_type, msg1, uid, chat_id, key, iv)
                                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                                
                                                # Part 2: Details
                                                msg2 = (
                                                    f"[FFFFFF]UID: {fix_num(target_uid)}\n"
                                                    f"[FFFFFF]Region: {region}\n"
                                                    f"[FFFFFF]Status: {ban_status[:25]}"
                                                )
                                                await asyncio.sleep(1.0)
                                                P = await SEndMsG(response.Data.chat_type, msg2, uid, chat_id, key, iv)
                                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                                print('🔥 [CHECK] ✅ All parts sent!')
                                        
                                        except Exception as e:
                                            print(f'🔥 [CHECK] ❌ Error: {e}')
                                            error_msg = "[B][C][FF0000]❌ Error occurred"
                                            P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                            
                            except Exception as e:
                                print(f'🔥 [CHECK] ❌ Exception: {e}')
                                error_msg = "[B][C][FF0000]❌ Command failed"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                        # /inv command - Invite spam
                        if inPuTMsG.startswith('/inv'):
                            CodE = inPuTMsG.split('/inv')[1]
                            try:
                                dd = chatdata['5']['data']['16']

                                async def squad_invite_cycle():
                                    try:
                                        PAc = await OpEnSq(key , iv,region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(3, CodE ,key, iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                        await asyncio.sleep(0.001)

                                        PAc = await OpEnSq(key , iv,region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(5, CodE ,key, iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                        await asyncio.sleep(0.001)

                                        PAc = await OpEnSq(key , iv,region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(6, CodE ,key, iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                        PAc = await OpEnSq(key , iv,region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(6, CodE ,key, iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                        PAc = await OpEnSq(key , iv,region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(6, CodE ,key, iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                        PAc = await OpEnSq(key , iv,region)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                        C = await cHSq(6, CodE ,key, iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                        V = await SEnd_InV(5 , CodE , key , iv,region)
                                        await asyncio.sleep(0.001)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                        E = await ExiT(None , key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                                    except Exception as e:
                                        print(f"Error inside squad_invite_cycle: {e}")

                         
                                invite_tasks = []
                                for _ in range(300): 
                                    task = asyncio.create_task(squad_invite_cycle())
                                    invite_tasks.append(task)
                                    await asyncio.sleep(0.001) 

                                # Wait for all tasks to complete
                                await asyncio.gather(*invite_tasks, return_exceptions=True)
                            except:
                                print('msg in squad')

                        

                           
                        # /lag command - ULTRA POWERFUL Lag attack on squad
                        if inPuTMsG.startswith('/lag'):
                                print(f'[LAG] Command received from UID: {uid}')
                                parts = inPuTMsG.strip().split()
                                
                                if len(parts) < 2:
                                    error_msg = f"[B][C][FF0000]\n\n❌ Usage: /lag TEAMCODE [N]\n[FFFFFF]Example: /lag teamcode 5\n[FFFF00]Max: 10 repeats\n"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                else:
                                    team_code = parts[1].upper()
                                    repeat_count = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 3
                                    if repeat_count > 10:
                                        repeat_count = 10
                                    
                                    total_packets = repeat_count * 100
                                    start_msg = f"[B][C][FF0000]💀 ULTRA LAG ATTACK 💀\n[FFFFFF]Code: {team_code}\n[FFFF00]Repeats: {repeat_count}\n[FFFF00]⚠️ EXTREME LAG!"
                                    P = await SEndMsG(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    
                                    for i in range(repeat_count):
                                 
                                        for j in range(100):
                                         
                                            for k in range(3):
                                                join_packet = await GenJoinSquadsPacket(team_code, key, iv)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                            
                                            await asyncio.sleep(0.0005) 
                                            
                                            
                                            for k in range(3):
                                                leave_packet = await ExiT(None, key, iv)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
                                            
                                            await asyncio.sleep(0.0001)     
                                        
                                      
                                        if i < repeat_count - 1:
                                            progress = (i + 1) * 100
                                            progress_msg = f"[B][C][FFFF00]⚡ Progress: {progress}/{total_packets} packets sent..."
                                            P = await SEndMsG(response.Data.chat_type, progress_msg, uid, chat_id, key, iv)
                                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                            await asyncio.sleep(0.05)
                                    
                                    success_msg = f"[B][C][00FF00]\n\n✅ ULTRA LAG COMPLETED!\n[FFFFFF]Code: {team_code}\n"
                                    P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    print(f'[LAG] Ultra attack completed - {total_packets * 6} packets')

                        # /start command - Start squad
                        if inPuTMsG.startswith('/start'):
                                print(f'[START] Command received from UID: {uid}')
                                parts = inPuTMsG.strip().split()
                                
                                if len(parts) < 2:
                                    error_msg = f"[B][C][FF0000]\n\n❌ Usage: /start TEAMCODE\n[FFFFFF]Example: /start ABC123\n"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                else:
                                    team_code = parts[1].upper()

                                    start_msg = f"[B][C]{get_random_color()}\n\n💥 Starting a squad...\nCode: {team_code}\n"
                                    P = await SEndMsG(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    
                                    join_packet = await GenJoinSquadsPacket(team_code, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                    import time
                                    attack_start = time.time()
                                    while time.time() - attack_start < 30:

                                        EM = await FS(key , iv)
                                        await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)

                                        
                                        await asyncio.sleep(0.15)

                                    success_msg = f"[B][C][00FF00]\n\n✅ Squad started!\nCode: {team_code}\n"
                                    P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    print(f'[START] Completed')

                        # /attack command -
                        if inPuTMsG.startswith('/attack'):
                                print(f'[ATTACK] Command received from UID: {uid}')
                                parts = inPuTMsG.strip().split()
                                
                                if len(parts) < 2:
                                    error_msg = f"[B][C][FF0000]\n\n❌ Usage: /attack TEAMCODE\n[FFFFFF]Example: /attack ABC123\n"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                else:
                                    team_code = parts[1].upper()
                                    
                                    start_msg = f"[B][C]{get_random_color()}\n\n💥 Starting attack...\nCode: {team_code}\n"
                                    P = await SEndMsG(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    
                                   
                                    import time
                                    attack_start = time.time()
                                    while time.time() - attack_start < 60:
                                        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                        
                                        leave_packet = await ExiT(None, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
                                        
                                        await asyncio.sleep(0.15)
                                    
                                    success_msg = f"[B][C][00FF00]\n\n✅ Attack completed!\nCode: {team_code}\n"
                                    P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    print(f'[ATTACK] Completed')
  




                        # /room command - ROOM SPAM (FAST SIMPLE FORMAT)
                        if inPuTMsG.startswith('/room'):
                            print(f'🔥 [ROOM] Command received from UID: {uid}')
                            parts = inPuTMsG.strip().split()
                            
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ Usage: /room ROOMID UID [COUNT]\n[FFFFFF]Example: /room 123456 12345678 50"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            else:
                                room_id = parts[1]
                                target_uid = parts[2]
                                spam_count = int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else 100
                                if spam_count > 500:
                                    spam_count = 500
                                
                          
                                loading_msg = f"[B][C][FFFF00]🏠 Sending {spam_count} room invites to {fix_num(target_uid)}..."
                                P = await SEndMsG(response.Data.chat_type, loading_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                print(f'🔥 [ROOM] Starting {spam_count} room spam to {target_uid}')
                                
                      
                                for i in range(spam_count):
                                    V = await SPam_Room(int(target_uid), int(room_id), "FARAZ BOT SPAM", key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.01)  
                                
                                await asyncio.sleep(1.0)
                         
                                success_msg = f"[B][C][00FF00]✅ ROOM SPAM COMPLETED!\n[FFFFFF]Room ID: {room_id}\n[FFFFFF]Target: {fix_num(target_uid)}\n[FFFFFF]Total: {spam_count} packets"
                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                print(f'🔥 [ROOM] ✅ SUCCESS: {spam_count} room packets sent')

                        # /spam command - Send spam requests via API (
                        if inPuTMsG.startswith('/spam'):
                                target_uid = None  
                                print(f'[SPAM] ═══════════════════════════════════════')
                                print(f'[SPAM] Command received from UID: {uid}')
                                print(f'[SPAM] Chat type: {response.Data.chat_type}')
                                print(f'[SPAM] Chat ID: {chat_id}')
                                parts = inPuTMsG.strip().split()
                                
                                if len(parts) < 2:
                                    error_msg = f"[B][C][FF0000]❌ Usage: /spam UID\n[FFFFFF]Example: /spam 12345678"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                else:
                                    target_uid = parts[1]
                                    print(f'[SPAM] Target UID: {target_uid}')
                                    
                                    loading_msg = f"[B][C][11EAFD]⏳ FRIEND REQUEST SPAM\n[FFFFFF]Target: {fix_num(target_uid)}\n[FFFFFF]Please wait 25 seconds..."
                                    P = await SEndMsG(response.Data.chat_type, loading_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    await asyncio.sleep(1.0)  
                                    print(f'[SPAM] Loading message sent, calling API...')
                                    
                                    try:
                                        result = await send_spam_api(target_uid)
                                        print(f'[SPAM] API Response: {result}')
                                        
                                        await asyncio.sleep(1.0)  
                                        if result["status"] == "ok":
                                         
                                            P = await SEndMsG(response.Data.chat_type, result["message"], uid, chat_id, key, iv)
                                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                            print(f'[SPAM] ✅ SUCCESS: Response sent for {target_uid}')
                                            
                                            # Add success confirmation
                                            await asyncio.sleep(1.0)
                                            success_msg = f"[B][C][00FF00]✅ Spam completed for {fix_num(target_uid)}!"
                                            P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                            print(f'[SPAM] ✅ SUCCESS: Confirmation sent')
                                        else:
                                            error_msg = f"[B][C][FF0000]❌ Spam API Error\n[FFFFFF]{result.get('message', 'Unknown error')}"
                                            P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                            print(f'[SPAM] ❌ ERROR: Failed for {target_uid}')
                                    
                                    except Exception as e:
                                        print(f'[SPAM] ❌ EXCEPTION: {e}')
                                        await asyncio.sleep(1.0)
                                        error_msg = f"[B][C][FF0000]❌ Spam failed: {str(e)}"
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                    
                                    print(f'[SPAM] ═══════════════════════════════════════')

                   


                        
                        # /info command - Get player info (name, UID, region, exp, LIKES, create time)
                        if inPuTMsG.startswith('/info'):
                            print(f'🔥 [INFO] ═══════════════════════════════════════')
                            print(f'🔥 [INFO] Command received from UID: {uid}')
                            print(f'🔥 [INFO] Chat type: {response.Data.chat_type}')
                            print(f'🔥 [INFO] Chat ID: {chat_id}')
                            parts = inPuTMsG.strip().split()
                            
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /info UID\n[FFFFFF]Example: /info 12345678"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                print(f'🔥 [INFO] Error message sent')
                            else:
                                target_uid = parts[1]
                                print(f'🔥 [INFO] Target UID: {target_uid}')
                                
                                # Loading message
                                loading_msg = f"[B][C][FFFF00]⏳ Getting info...\n[FFFFFF]Target: {fix_num(target_uid)}"
                                P = await SEndMsG(response.Data.chat_type, loading_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                await asyncio.sleep(1.0)
                                print(f'🔥 [INFO] Loading message sent')
                                
                                try:
                                    # Call API
                                    info_response = await check_player_info(target_uid)
                                    print(f'🔥 [INFO] Raw API Response: {info_response}')
                                    
                                    if info_response.get('status') == 'ok':
                                        player_data = info_response.get('data', {})
                                        basic_info = player_data.get('basicInfo', {})
                                        
                                        # Extract all fields including LIKES
                                        name = basic_info.get('nickname', 'Unknown')
                                        region = basic_info.get('region', 'bd')
                                        exp = basic_info.get('exp', 0)
                                        likes = basic_info.get('liked', 0)  
                                        
                                
                                        create_timestamp = basic_info.get('createAt', None)
                                        if create_timestamp:
                                            try:
                                                from datetime import datetime
                                                create_date = datetime.fromtimestamp(int(create_timestamp))
                                                create_time = create_date.strftime('%Y-%m-%d')
                                            except:
                                                create_time = 'Unknown'
                                        else:
                                            create_time = 'Unknown'
                                        
                                        print(f'🔥 [INFO] Parsed - Name: {name}, Region: {region}, EXP: {exp}, Likes: {likes}, Created: {create_time}')
                                        
                                        
                                        await asyncio.sleep(2.0)  # Wait 2 seconds before starting
                                        msg1 = f"[B][C][00FF00]✅ PLAYER INFO\n[FFFFFF]━━━━━━━━━━━━━━\n[FFFF00]Name: [FFFFFF]{name}\n[FFFF00]UID: [FFFFFF]{fix_num(target_uid)}"
                                        P1 = await SEndMsG(response.Data.chat_type, msg1, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P1)
                                        print(f'🔥 [INFO] Part 1 sent (Name + UID)')
                                        
                                        await asyncio.sleep(2.5)  
                                        msg2 = f"[B][C][FFFF00]Region: [FFFFFF]{region.upper()}\n[FFFF00]EXP: [FFFFFF]{fix_num(exp)}\n[FFFF00]Likes: [FFFFFF]{fix_num(likes)}"
                                        P2 = await SEndMsG(response.Data.chat_type, msg2, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P2)
                                        print(f'🔥 [INFO] Part 2 sent (Region + EXP + Likes)')
                                        
                                        await asyncio.sleep(2.5)  
                                        msg3 = f"[B][C][00FF00]Created: [FFFFFF]{create_time}\n[FFFFFF]━━━━━━━━━━━━━━"
                                        P3 = await SEndMsG(response.Data.chat_type, msg3, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P3)
                                        print(f'🔥 [INFO] Part 3 sent (Created date)')
                                        
                                        print(f'🔥 [INFO] ✅ ALL 3 INFO PARTS SENT WITH PROPER DELAYS!')
                                    else:
                                        await asyncio.sleep(1.0)
                                        error_msg = f"[B][C][FF0000]❌ Player not found\n[FFFFFF]UID: {fix_num(target_uid)}"
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        print(f'🔥 [INFO] Error: Player not found')
                                
                                except Exception as e:
                                    print(f'🔥 [INFO] ❌ EXCEPTION: {e}')
                                    import traceback
                                    traceback.print_exc()
                                    await asyncio.sleep(1.0)
                                    error_msg = f"[B][C][FF0000]❌ API Error\n[FFFFFF]{str(e)[:50]}"
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                
                                print(f'🔥 [INFO] ═══════════════════════════════════════')
                        if inPuTMsG.strip().startswith('/s1'):
                            await handle_badge_command('s1', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
    
                        if inPuTMsG.strip().startswith('/s2'):
                            await handle_badge_command('s2', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s3'):
                            await handle_badge_command('s3', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s4'):
                            await handle_badge_command('s4', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s5'):
                            await handle_badge_command('s5', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)    

                        # @EVOS - START EVOLUTION CYCLE WATASHII IS HERE
                        if inPuTMsG.strip().startswith('/evos'):
                            global evo_cycle_running, evo_cycle_task
                            print('Processing evo cycle start command')
    
                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use sender's UID
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:
                                        uids.append(part)
                                        print(f"Added UID: {part}")

                            # Stop existing cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(
                                evo_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][00FF00]✅ Evolution cycle started!\n🎯 Target: You\n🎭 Emotes: All 18 evo emotes\n⏰ Delay: 5s between emotes\n🔄 Loop until @sevos\n"
                            else:
                                success_msg = f"[B][C][00FF00]✅ Evolution cycle started!\n🎯 Targets: You + {len(uids)-1} players\n🎭 Emotes: All 18 evo emotes\n⏰ Delay: 5s\n🔄 Loop until @sevos\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region)
                            print(f"Started evo cycle for: {uids}")
                        
                        # @SEVOS - STOP EVOLUTION CYCLE WATASHII IS HERE
                        if inPuTMsG.strip() == '/sevos':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ Evolution cycle stopped!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region)
                                print("Evolution cycle stopped")
                            else:
                                error_msg = f"[B][C][FF0000]❌ No active evo cycle to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region)                               
                        
                        

                        # /ai command - AI interaction using free Gemini API
                        if inPuTMsG.startswith('/ai'):
                            print(f'[AI] ═══════════════════════════════════════')
                            print(f'[AI] Command received from UID: {uid}')
                            
                            parts = inPuTMsG.split('/ai', 1)
                            if len(parts) < 2 or not parts[1].strip():
                                error_msg = "[B][C][FF0000]❌ Usage: /ai QUESTION\n[FFFFFF]Example: /ai What is Free Fire?"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            else:
                                question = parts[1].strip()
                                print(f'[AI] Question: {question}')
                                
                                # Loading message
                                loading_msg = f"[B][C][FFFF00]🤖 Connecting Ai..."
                                P = await SEndMsG(response.Data.chat_type, loading_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                await asyncio.sleep(1.0)
                                
                                try:
                                    # Call free Gemini API (no key required)
                                    api_url = f"https://botfather.cloud/Apis/AI/client.php?message={question}"
                                    
                                    async with aiohttp.ClientSession() as session:
                                        async with session.get(
                                            api_url,
                                            timeout=aiohttp.ClientTimeout(total=20)
                                        ) as ai_response:
                                            if ai_response.status == 200:
                                                ai_data = await ai_response.json()
                                                ai_text = ai_data.get('response', 'No response from AI')
                                                
                                           
                                                max_chunk = 200
                                                chunks = [ai_text[i:i+max_chunk] for i in range(0, len(ai_text), max_chunk)]
                                                
                                                for i, chunk in enumerate(chunks[:3]):  # Max 3 parts
                                                    await asyncio.sleep(1.0)
                                                    ai_msg = f"[B][C][00FF00]🤖 AI ({i+1}/{min(len(chunks), 3)}):\n[FFFFFF]{chunk}"
                                                    P = await SEndMsG(response.Data.chat_type, ai_msg, uid, chat_id, key, iv)
                                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                                    print(f'[AI] Part {i+1}/{min(len(chunks), 3)} sent')
                                                
                                                print(f'[AI] ✅ Response sent successfully')
                                            else:
                                                error_msg = f"[B][C][FF0000]AI feature temporarily disabled. Function 'talk_with_ai' not implemented."
                                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                                print(f'[AI] AI feature temporarily disabled. Function  not implemented.')
                                
                                except Exception as e:
                                    print(f'[AI] ❌ Exception: {e}')
                                    error_msg = f"[B][C][FF0000]AI feature temporarily disabled. Function  not implemented."
                                    P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            
                            print(f'[AI] ═══════════════════════════════════════')
                        

                        

                        
               
                        if inPuTMsG in ("hi" , "hello" , "fen" , "salam"):
                            uid = response.Data.uid
                            chat_id = response.Data.Chat_ID
                            message = 'ASSALAMU_ALAIKUM Im Watashii\nDiscord : im9p.'

                            P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                        response = None
                            
            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    Uid , Pw = '4433764355' ,'EC4F0F3C5E201B161DD907C6C1AC72A0F2A0C3DA34778DCFC71B1B107FBC1D0F'  # <- HeRe YouR AccounT ID anD PassWorD



    open_id , access_token = await GeNeRaTeAccEss(Uid , Pw)
    if not open_id or not access_token: print("ErroR - InvaLid AccounT") ; return None
    
    PyL = await EncRypTMajoRLoGin(open_id , access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE: print("TarGeT AccounT => BannEd / NoT ReGisTeReD ! ") ; return None
    
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    print(UrL)
    region = MajoRLoGinauTh.region

    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    LoGinDaTa = await GetLoginData(UrL , PyL , ToKen)
    if not LoGinDaTa: print("ErroR - GeTinG PorTs From LoGin DaTa !") ; return None
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    

    

    try:
        if OnLinePorTs.count(':') > 1:
       
            parts = OnLinePorTs.rsplit(':', 1)
            OnLineiP = parts[0]
            OnLineporT = parts[1] if len(parts) > 1 else '39800'
        else:
            OnLineiP , OnLineporT = OnLinePorTs.split(":")
        
        if ChaTPorTs.count(':') > 1:

            parts = ChaTPorTs.rsplit(':', 1)
            ChaTiP = parts[0]
            ChaTporT = parts[1] if len(parts) > 1 else '39700'
        else:
            ChaTiP , ChaTporT = ChaTPorTs.split(":")
        
        print(f"[DEBUG] Parsed - OnLine: {OnLineiP}:{OnLineporT}")
        print(f"[DEBUG] Parsed - Chat: {ChaTiP}:{ChaTporT}")
    except Exception as e:
        print(f"[ERROR] Failed to parse ports: {e}")
        return None
    
    acc_name = LoGinDaTaUncRypTinG.AccountName

    print(ToKen)
    equie_emote(ToKen,UrL)
    AutHToKen = await xAuThSTarTuP(int(TarGeT) , ToKen , int(timestamp) , key , iv)
    ready_event = asyncio.Event()
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT , AutHToKen , key , iv , LoGinDaTaUncRypTinG , ready_event ,region))
     
    await ready_event.wait()
    await asyncio.sleep(1)
    task2 = asyncio.create_task(TcPOnLine(OnLineiP , OnLineporT , key , iv , AutHToKen))
    os.system('cls')
    print(render(' XBLACK IS HERE', colors=['white', 'green'], align='center'))
    print('')

    print(f" - BoT STarTinG And OnLine on TarGet : {TarGeT} | BOT NAME : {acc_name}\n")
    print(f" - BoT sTaTus > GooD | OnLinE ! (:")    
    await asyncio.gather(task1 , task2)
    
async def StarTinG():
    while True:
        try: await asyncio.wait_for(MaiiiinE() , timeout = 7 * 60 * 60)
        except asyncio.TimeoutError: print("Token ExpiRed ! , ResTartinG")
        except Exception as e: print(f"ErroR TcP - {e} => ResTarTinG ...")

if __name__ == '__main__':
    asyncio.run(StarTinG())