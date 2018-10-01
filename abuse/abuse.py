import random
import json
import unirest


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

    words = [i for i in DATASET if i.lower().startswith(data_in.lower())]
    if not words:
        return None
    return random.choice(words)


def listAnyAbuse():
    """ Returns any random abuse from it's built-in dataset. """
    return random.choice(DATASET)


def listAllAbuses():
    """ Just returns all the abusive words present in the dataset. """
    return dataset


def meaning(word):
        response = unirest.get("https://mashape-community-urban-dictionary.p.mashape.com/define?term=%s" %word,
        headers={"X-Mashape-Key": "zrjVVm5FQkmshdqfscSnmDPbHaaep1reMKyjsntWZRKe8jAoUm",
                 "Accept": "text/plain"
                }
        )
        json_data = response.body
        json_data_neat=json.dumps([json_data], separators=(',',':'))
        jsonofabitch = json.loads(json_data_neat)
        return (jsonofabitch[0]['list'][0]['definition']

__all__ = ('listAbusesFrom', 'randomAbuseFrom', 'listAllAbuse', 'listAnyAbuse','meaning')
