import random


DATASET = ['anus', 'arse', 'arsehole', 'ass', 'ass-hat', 'ass-jabber', 'ass-pirate', 'assbag', 'assbandit', 'assbanger', 'assbite', 'assclown', 'asscock', 'asscracker', 'asses', 'assface', 'assfuck', 'assfucker', 'assgoblin', 'asshat', 'asshead', 'asshole', 'asshopper', 'assjacker', 'asslick', 'asslicker', 'assmonkey', 'assmunch', 'assmuncher', 'assnigger', 'asspirate', 'assshit', 'assshole', 'asssucker', 'asswad', 'asswipe', 'axwound', 'bampot', 'bastard', 'beaner', 'bitch', 'bitchass', 'bitches', 'bitchtits', 'bitchy', 'blow job', 'blowjob', 'bollocks', 'bollox', 'boner', 'brotherfucker', 'bullshit', 'bumblefuck', 'butt plug', 'butt-pirate', 'buttfucka', 'buttfucker', 'camel toe', 'carpetmuncher', 'chesticle', 'chinc', 'chink', 'choad', 'chode', 'clit', 'clitface', 'clitfuck', 'clusterfuck', 'cock', 'cockass', 'cockbite', 'cockburger', 'cockface', 'cockfucker', 'cockhead', 'cockjockey', 'cockknoker', 'cockmaster', 'cockmongler', 'cockmongruel', 'cockmonkey', 'cockmuncher', 'cocknose', 'cocknugget', 'cockshit', 'cocksmith', 'cocksmoke', 'cocksmoker', 'cocksniffer', 'cocksucker', 'cockwaffle', 'coochie', 'coochy', 'coon', 'cooter', 'cracker', 'cum', 'cumbubble', 'cumdumpster', 'cumguzzler', 'cumjockey', 'cumslut', 'cumtart', 'cunnie', 'cunnilingus', 'cunt', 'cuntass', 'cuntface', 'cunthole', 'cuntlicker', 'cuntrag', 'cuntslut', 'dago', 'damn', 'deggo', 'dick', 'dick-sneeze', 'dickbag', 'dickbeaters', 'dickface', 'dickfuck', 'dickfucker', 'dickhead', 'dickhole', 'dickjuice', 'dickmilk', 'dickmonger', 'dicks', 'dickslap', 'dicksucker', 'dicksucking', 'dicktickler', 'dickwad', 'dickweasel', 'dickweed', 'dickwod', 'dike', 'dildo', 'dipshit', 'doochbag', 'dookie', 'douche', 'douche-fag', 'douchebag', 'douchewaffle', 'dumass', 'dumb ass', 'dumbass', 'dumbfuck', 'dumbshit', 'dumshit', 'dyke', 'fag', 'fagbag', 'fagfucker', 'faggit', 'faggot', 'faggotcock', 'fagtard', 'fatass', 'fellatio', 'feltch', 'flamer', 'fuck', 'fuckass', 'fuckbag', 'fuckboy', 'fuckbrain', 'fuckbutt', 'fuckbutter', 'fucked', 'fucker', 'fuckersucker', 'fuckface', 'fuckhead', 'fuckhole', 'fuckin', 'fucking', 'fucknut', 'fucknutt', 'fuckoff', 'fucks', 'fuckstick', 'fucktard', 'fucktart', 'fuckup', 'fuckwad', 'fuckwit', 'fuckwitt', 'fudgepacker', 'gay', 'gayass', 'gaybob', 'gaydo', 'gayfuck', 'gayfuckist', 'gaylord', 'gaytard', 'gaywad', 'goddamn', 'goddamnit', 'gooch', 'gook', 'gringo', 'guido', 'handjob', 'hard on', 'heeb', 'hell', 'hoe', 'homo', 'homodumbshit', 'honkey', 'humping', 'jackass', 'jagoff', 'jap', 'jerk off', 'jerkass', 'jigaboo', 'jizz', 'jungle bunny', 'junglebunny', 'kike', 'kooch', 'kootch', 'kraut', 'kunt', 'kyke', 'lameass', 'lardass', 'lesbian', 'lesbo', 'lezzie', 'mcfagget', 'mick', 'minge', 'mothafucka', "mothafuckin\\'", 'motherfucker', 'motherfucking', 'muff', 'muffdiver', 'munging', 'negro', 'nigaboo', 'nigga', 'nigger', 'niggers', 'niglet', 'nut sack', 'nutsack', 'paki', 'panooch', 'pecker', 'peckerhead', 'penis', 'penisbanger', 'penisfucker', 'penispuffer', 'piss', 'pissed', 'pissed off', 'pissflaps', 'polesmoker', 'pollock', 'poon', 'poonani', 'poonany', 'poontang', 'porch monkey', 'porchmonkey', 'prick', 'punanny', 'punta', 'pussies', 'pussy', 'pussylicking', 'puto', 'queef', 'queer', 'queerbait', 'queerhole', 'renob', 'rimjob', 'ruski', 'sand nigger', 'sandnigger', 'schlong', 'scrote', 'shit', 'shitass', 'shitbag', 'shitbagger', 'shitbrains', 'shitbreath', 'shitcanned', 'shitcunt', 'shitdick', 'shitface', 'shitfaced', 'shithead', 'shithole', 'shithouse', 'shitspitter', 'shitstain', 'shitter', 'shittiest', 'shitting', 'shitty', 'shiz', 'shiznit', 'skank', 'skeet', 'skullfuck', 'slut', 'slutbag', 'smeg', 'snatch', 'spic', 'spick', 'splooge', 'spook', 'suckass', 'tard', 'testicle', 'thundercunt', 'tit', 'titfuck', 'tits', 'tittyfuck', 'twat', 'twatlips', 'twats', 'twatwaffle', 'unclefucker', 'va-j-j', 'vag', 'vagina', 'vajayjay', 'vjayjay', 'wank', 'wankjob', 'wetback', 'whore', 'whorebag', 'whoreface', 'wop']
# dataset created by scrapping https://www.noswearing.com/dictionary/

def listAbusesFrom(data_in):
    """ Returns list of abuses starting from a specific letter provided in argument of the function. """
    if not isinstance(data_in, str):
        raise ValueError("data_in must be a string")

    words = [i for i in DATASET if i.lower().startswith(data_in.lower())]
    return words

def randomAbuseFrom(data_in):
    """ Returns a random abuse starting from a specific letter provided in argument of the function. """
    if not isinstance(data_in, str):
        raise ValueError("data_in must be a string")

    nicks = [i for i in DATASET if i.lower().startswith(data_in.lower())]
    if not nicks:
        return None
    return random.choice(nicks)

def listAnyAbuse():
    """ Returns any random abuse from it's built-in dataset. """
    return random.choice(DATASET)


def listAllAbuses():
    """ Just returns all the abusive words present in the dataset. """
    return list(DATASET)  # Cast to list to make a copy


"""Nicknames"""
DATASET_NICK = ["Fuckstick","Cockmuppet","Assclown","Douchemonger","Twat","Mouth-breather","Cockshiner","Cheesedick-Fuckface","Knuckle-dragger","Herb-Shitstick-Tool","Shitbag","Carpet-cleaner","Asshat","Slutbag","Numbnuts","Dicknose","Cum-dumpster","Weaksauce","Sleezebag","Buttmunch","Twatwaffle","Tard","Cunt-rag","Cuntmuscle","Shitstain","Dickbreath","Jizztissue","Cockgobbler","Cuntkicker","Douchenozzle","Pigfucker","Butknuckler","Clitsplitter","Shitshaker","Rumpleforeskin","Douche-canoe","Fuckrag","Rumpranger","Cock-juggling-thundercunt"]
# initial dataset created by scrapping https://top-funny-jokes.com/funny-insulting-names/

def listNicksFrom(data_in):
    """ Returns list of abuses starting from a specific letter provided in argument of the function. """
    if not isinstance(data_in, str):
        raise ValueError("data_in must be a string")

    nicks = [i for i in DATASET_NICK if i.lower().startswith(data_in.lower())]
    return nicks


def randomNicksFrom(data_in):
    """ Returns a random nicknames starting from a specific letter provided in argument of the function. """
    if not isinstance(data_in, str):
        raise ValueError("data_in must be a string")

    nicks = [i for i in DATASET_NICK if i.lower().startswith(data_in.lower())]
    if not nicks:
        return None
    return random.choice(nicks)

def listAnyNicks():
    """ Returns any random nicknames from it's built-in dataset. """
    return random.choice(DATASET_NICK)

def listAllNicks():
    """ Just returns all the abusive nicknames present in the dataset. """
    return list(DATASET_NICK)  # Cast to list to make a copy




__all__ = ('listAbusesFrom', 'randomAbuseFrom', 'listAllAbuse', 'listAnyAbuse','listNickFrom','randomAbuseFrom','listAnyNicks','listAllNick')
