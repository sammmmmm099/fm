import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "12655645")
    API_HASH  = os.environ.get("API_HASH", "05c4cafe00b81ed83207bb4365e0053b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7900540474:AAGM-VFZbFJ0t-16EelYsutowr4GlhizTwY") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","temp")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://sainallamilli:Filestore1@cluster0.8urcp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
   
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/7Bt.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1074804932 1077880102').split()]
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'pspkbots,Animes2u').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002551557488"))
    NEW_USER_LOG = int(os.environ.get("NEW_USER_LOG", "-1002551557488"))
         
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
        
    START_TXT = """<b>Aʜᴏʏ {} ⚔️!

Welcome to this bot! Whether it's the best or the worst bot from @Elites_Bots, let's see if we can make it something truly amazing!

──────────────────</b>"""
