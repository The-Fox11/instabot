from instabot import Bot
import time

# Fonction pour liker le dernier reel d'un utilisateur
def like_latest_reel(bot, username):
    user_id = bot.get_user_id_from_username(username)
    media_ids = bot.get_user_medias(user_id, filtration=True)
    if media_ids:
        # Trouver le dernier reel
        latest_reel = media_ids[0]
        bot.like(latest_reel)
        print(f"Liked reel {latest_reel} from {username}")
    else:
        print("No reels found.")

# Créer une instance du bot et se connecter avec les comptes bot
def main():
    # Informations de connexion
    accounts = [
        {'username': 'nilsdisot', 'password': 'De@thguy22'},
        {'username': 'max.frene', 'password': 'De@thguy22'}
    ]
    
    reel_user = 'lindsay.chlo22'

    for account in accounts:
        bot = Bot()
        bot.login(username=account['username'], password=account['password'])
        
        # Liker le dernier reel de l'utilisateur cible
        like_latest_reel(bot, reel_user)
        
        # Attendre un peu avant de passer au prochain compte
        print(f"Sleeping for 10 seconds before switching accounts.")
        time.sleep(10)

if __name__ == "__main__":
    main()
