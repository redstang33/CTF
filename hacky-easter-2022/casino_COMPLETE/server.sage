from random import randint
#from secrets import flag
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad

class RNG:
    def __init__(self):
        p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
        b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
        self.curve = EllipticCurve(GF(p), [-3,b])

        self.P = self.curve.lift_x(15957832354939571418537618117378383777560216674381177964707415375932803624163)
        self.Q = self.curve.lift_x(66579344068745538488594410918533596972988648549966873409328261501470196728491)

        self.state = randint(1, 2**256)

    def next(self):
        r = (self.state * self.P)[0].lift()
        self.state = (r * self.P)[0].lift()
        return (r * self.Q)[0].lift() >> 8

    def prsta(self):
        print(self.state)

class Casino:
    def __init__(self, rng):
        self.rng = rng
        self.balance = 10

    def play(self):
        print("Your bet: ", end='')
        bet = input()
        if (bet in ["0", "1"]):
            bet = Integer(bet)
            nr = self.rng.next()
            print(nr)
            if (nr % 2 == bet):
                self.balance += 1
            else:
                self.balance -= 1
                if (self.balance == 0):
                    print("You are broke... play again")
                    exit()
            print(f"Your current balance: {self.balance}")
        else:
            print("Invalid bet option, use either 0 or 1")

    def buy_flag(self):
        if (self.balance >= 1337):
            key = SHA256.new(str(self.rng.next()).encode('ascii')).digest()
            cipher = AES.new(key, AES.MODE_ECB)
            print(cipher.encrypt(pad(flag.encode('ascii'), 16)).hex())
        else:
            print("No flag for the poor. Gamble more")



def main():
    rng = RNG()
    casino = Casino(rng)

    def do_next(s):
        sP = s * P
        r = Integer(sP[0])
        s_new = Integer((r * P)[0])
        rQ = r * Q
        return Integer(rQ[0]), s_new

    def do_guess(r1):
        try:
            rQ1 = E.lift_x(r1)
        except ValueError:
            return None
        sP2 = d * rQ1
        s2 = Integer(sP2[0])
        r2, s3 = do_next(s2)
        return r2, s2, s3
    # def do_guess(r1):
    #     try:
    #         s = P // r1


    print("Welcome to the Casino")
    r1=rng.next()
    print(f"Your id is "+ str(r1))
    print("What would you like to do?")
    print("(p)lay and win some money")
    print("(b)uy the flag")
    print("(s)how the state")

    while (True):
        print("> ", end='')
        option = input()

        if (not option in ["b", "p", "s", "y", "z", "o", "e"]):
            print("Unknown option, use 'b' or 'p'")
        elif (option == "b"):
            casino.buy_flag()
        elif (option == "p"):
            casino.play()
        elif (option == "s"):
            rng.prsta()
        elif (option == "y"):
            print(dict_i)
        elif (option == "o"):
            for x in list(dict_i):
                if dict_i[x] % 2 == 0:
                    dict_i.pop(x)
            for x in list(dict_i):
                guess = do_guess(x)
                if guess:
                    r2_guess, s2 = guess
                    r2_guess = r2_guess >> 8
                    dict_i[s2] = r2_guess
                    dict_i.pop(x)
        elif (option == "e"):
            for x in list(dict_i):
                if dict_i[x]%2 == 1:
                    dict_i.pop(x)
            for x in list(dict_i):
                guess = do_guess(x)
                if guess:
                    r2_guess, s2 = guess
                    r2_guess = r2_guess >> 8
                    dict_i[s2] = r2_guess
                    dict_i.pop(x)


        elif (option == "z"):
            p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
            b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
            E = EllipticCurve(GF(p), [-3,b])
            P = E.lift_x(15957832354939571418537618117378383777560216674381177964707415375932803624163)
            Q = E.lift_x(66579344068745538488594410918533596972988648549966873409328261501470196728491)
            # P = dQ
            d = Q.discrete_log(P)

            # r1_guess, r2, s2, s3 = do_guess(r1_guess)
            # print(do_guess(r1_guess))
            # print(r1_guess, r2, s2, s3)
            #
            dict_i = {}
            for i in range(2 ** 8):
                r1_guess = (r1 << 8) + i
                guess = do_guess(r1_guess)
                if guess:
                    r2_guess, s2, s3 = guess
                    r2_guess = r2_guess >> 8
                    dict_i[i] = [r2_guess, s2, s3]


if __name__ == '__main__':
    main()
