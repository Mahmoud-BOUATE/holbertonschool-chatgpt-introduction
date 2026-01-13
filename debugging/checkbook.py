#!/usr/bin/python3

class Checkbook:
    """
    Classe : Checkbook
    Représente un compte bancaire simple avec dépôt, retrait et consultation du solde.
    """

    def __init__(self):
        """
        Initialise un compte avec un solde de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant sur le compte.

        Paramètres :
        amount (float) : Montant à déposer (doit être positif).

        Retourne :
        None
        """
        if amount < 0:
            print("Le montant à déposer doit être positif.")
            return
        self.balance += amount
        print("Déposé : ${:.2f}".format(amount))
        print("Solde actuel : ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant du compte si le solde est suffisant.

        Paramètres :
        amount (float) : Montant à retirer (doit être positif).

        Retourne :
        None
        """
        if amount < 0:
            print("Le montant à retirer doit être positif.")
            return
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Retiré : ${:.2f}".format(amount))
            print("Solde actuel : ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du compte.

        Retourne :
        None
        """
        print("Solde actuel : ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale qui permet à l'utilisateur d'interagir avec le checkbook.
    Gère les commandes : deposit, withdraw, balance, exit
    Ajoute la gestion des erreurs pour les entrées invalides.
    """
    cb = Checkbook()
    while True:
        action = input("Que voulez-vous faire ? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Merci d'avoir utilisé le checkbook. Au revoir !")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Entrez le montant à déposer : $"))
                cb.deposit(amount)
            except ValueError:
                print("Entrée invalide ! Veuillez entrer un nombre valide.")
        elif action == 'withdraw':
            try:
                amount = float(input("Entrez le montant à retirer : $"))
                cb.withdraw(amount)
            except ValueError:
                print("Entrée invalide ! Veuillez entrer un nombre valide.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
