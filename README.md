# Archive of Sieberrsec CTF 3.0

Challenges were archived after the CTF from [ctfx.sieberrsec.tech](https://ctfx.sieberrsec.tech), with edits made to some challenge descriptions in `challenges.json` to remove and move source code to their respective locations in the `files` directory (marked out by `[SOURCE CODE]`). Challenge files should also be also available there, since links to files (especially those hosted on the platform) may break.

*Note: Some files are split into mutliple smaller files due to GitHub's file size limit, reassemble in 7-Zip using `Combine files...` or `cat filename.zip.* > filename.zip`.*

Writeups are available [here]().

[PWN](#pwn)

- [simple](#simple)
- [warmup](#warmup)
- [malloc](#malloc)
- [rock farm simulator 2011](#rock-farm-simulator-2011)
- [Turbo Fast Crypto, part 2](#turbo-fast-crypto-part-2)

[CRYPTO](#crypto)

- [Shalom Shalom](#shalom-shalom)
- [Turbo Fast Crypto, part 1](#turbo-fast-crypto-part-1)
- [I can't open this file? Part 2](#i-cant-open-this-file-part-2)
- [Diffie's Key Exchange](#diffies-key-exchange)
- [I can't open this file? Part 1](#i-cant-open-this-file-part-1)
- [totallyfoolproofcrypto](#totallyfoolproofcrypto)
- [Diffie's Key Exchange 2](#diffies-key-exchange-2)
- [whodunnit](#whodunnit)

[RE](#re)

- [Flag checker](#flag-checker)
- [Reverse](#reverse)
- [Flag checker v2.0](#flag-checker-v20)

[OSINT](#osint)

- ["The Sieberr" Heist Part 1](#the-sieberr-heist-part-1)
- [A Wealth of Information Part 1](#a-wealth-of-information-part-1)
- [We go way back](#we-go-way-back)
- [A Wealth of Information Part 2](#a-wealth-of-information-part-2)
- ["The Sieberr" Heist Part 3](#the-sieberr-heist-part-3)
- ["The Sieberr" Heist Part 2](#the-sieberr-heist-part-2)
- [Public Transport Hunt](#public-transport-hunt)

[WEB](#web)

- [[Part 1] FUTURE TECHNOLOGIES AI IOT FOURTH INDUSTRIAL REVOLUTION SECURITY CAMERA](#part-1-future-technologies-ai-iot-fourth-industrial-revolution-security-camera)
- [[Part 2] FUTURE TECHNOLOGIES AI IOT FOURTH INDUSTRIAL REVOLUTION SECURITY CAMERA](#part-2-future-technologies-ai-iot-fourth-industrial-revolution-security-camera)
- [TaiYang IT Solution Part 1](#taiyang-it-solution-part-1)
- [Exploring The Universe! (Part 1)](#exploring-the-universe-part-1)
- [TaiYang IT Solution Part 2: Electric Boogaloo](#taiyang-it-solution-part-2-electric-boogaloo)

[FORENSICS](#forensics)

- [Duck Delivery](#duck-delivery)
- [Birds?](#birds)
- [Digging In The Dump Pt. I](#digging-in-the-dump-pt-i)
- [Digging In The Dump Pt. II](#digging-in-the-dump-pt-ii)
- [Mind Cracking Adversity](#mind-cracking-adversity)
- [Exploring The Universe! (Part 2)](#exploring-the-universe-part-2)
- [plush, lush, flush, blush](#plush-lush-flush-blush)

[MISC](#misc)

- [Heads and Tails Part 1](#heads-and-tails-part-1)
- [Heads and Tails Part 2](#heads-and-tails-part-2)
- [Heads and Tails Part 3](#heads-and-tails-part-3)
- [Can You Math It?](#can-you-math-it)
- [I lost my anime collection! Pt. II](#i-lost-my-anime-collection-pt-ii)
- [I lost my anime collection! Pt. I](#i-lost-my-anime-collection-pt-i)
- [rock farming simulator deluxe edition](#rock-farming-simulator-deluxe-edition)

[SANITY](#sanity)

- [sanity check](#sanity-check)

---

## PWN

### simple

Points: 62
Solves: 47
Author: chowgz

Flag: IRS{W377_D0NE_40U_G3N1u5_WBVAVEF}

#### Description

> Simple game right?
>
> `nc challs.sieberrsec.tech 8862`
>
> ```c
> #include <stdio.h>
> #include <stdlib.h>
> 
> // cc simple.c -o simple -fstack-protector-all
> int main(void)
> {
> 	puts("Want a flag? Just play until you win!");
> 	puts("Goal: Become a billionaire!");
> 	int account_value = 1000000;
> 	while (account_value < 1000000000) {
> 		printf("\nAccount value: $%d\n", account_value);
> 		puts("Commands:");
> 		puts("1. Withdraw money");
> 		puts("2. Deposit money");
> 		printf("Choose an option [1/2]: ");
> 		int option = 0;
> 		scanf("%d", &option);
> 		while (option != 1 && option != 2) {
> 			puts("Invalid option!");
> 			printf("Choose an option [1/2]: ");
> 			scanf("%d", &option);
> 		}
> 		if (option == 1) {
> 			printf("Amount to withdraw: ");
> 			int withdrawal = 0;
> 			scanf("%d", &withdrawal);
> 			account_value -= withdrawal;
> 		} else {
> 			puts("LOL no you are not allowed to deposit money. :(");
> 		}
> 	}
> 	printf("\nAccount value: $%d\n", account_value);
> 	system("cat flag");
> 	return 0;
> }
> ```

### warmup

Points: 316
Solves: 17
Author: main

Flag: IRS{nU1L_t3rminat0r}

#### Description

> Just a warmup. `nc challs.sieberrsec.tech 3476`
>
> ```c
> #include <stdio.h>
> int main() {
>     char input[32];
>     char flag[32];
>     // read flag file
>     FILE *f = fopen("flag", "r");
>     fgets(flag, 32, f);
>     fclose(f);
>     // read the user's guess
>     fgets(input, 0x32, stdin);
>     // if user's guess matches the flag
>     if (!strcmp(flag,input)) {
>         puts("Predicted!");
>         system("cat flag");
>     } else puts("Your flag was wrong :(");
> }
> ```
>
> N.B. please do not try to bruteforce the flag. Attempts at doing so will be taken as an attack on server infrastructure, and will leave you liable for disqualification.

Hint 1: https://ctf101.org/binary-exploitation/buffer-overflow/

Hint 2: https://en.wikipedia.org/wiki/Null-terminated_string

### malloc

Points: 400
Solves: 2
Author: chowgz

Flag: 

#### Description

> Can you somehow get the flag? Have fun!
>
> `nc challs.sieberrsec.tech 1470`
>
> ```c
> #include <unistd.h>
> 
> #include <stdio.h>
> #include <stdlib.h>
> 
> // cc malloc.c -o malloc -fstack-protector-all
> int main(void)
> {
> 	// Variables
> 	int *arr; // int pointer to an array
> 	char *msg; // C-string to store your message
> 	size_t length = 0;
> 	
> 	// Welcome message
> 	puts("Welcome to Sieberrsec CTF!");
> 	
> 	// Allocates 123456 bytes of memory
> 	arr = (int *)malloc(123456);
> 	
> 	// Sets first element of arr to 1
> 	arr[0] = 1;
> 	
> 	// Leaks the memory address of arr
> 	printf("Leak: %p\n", arr);
> 	
> 	// Gets length of your message
> 	printf("Length of your message: ");
> 	scanf("%lu", &length);
> 	
> 	// Allocates memory to store your message as a C-string
> 	// +1 is to store the null-byte that ends the string
> 	msg = malloc(length + 1);
> 	
> 	// Reads length bytes of input into msg
> 	printf("Enter your message: ");
> 	read(0, msg, length);
> 	
> 	// Null-byte to end the string
> 	msg[length] = 0;
> 	
> 	// Write length bytes from msg
> 	write(1, msg, length);
> 	
> 	// Your goal: somehow make arr[0] == 0
> 	if (arr[0] == 0) {
> 		system("cat flag");
> 	}
> 	return 0;
> }
> ```

### rock farm simulator 2011

Points: 799
Solves: 2
Author: main

Flag: IRS{so_long_space_pony}

#### Description

> Rocks, ponies, and all the time in the world! Can you get the Princess' flag?
> 
> `ssh -p 15233 rock_farming_simulator@challs.sieberrsec.tech`
> 
> Source code can be found [here](https://drive.google.com/uc?id=14u8ggvJEZxHMwIaFBFsw2YqmP-DVHfiH&export=download)
> 
> 
> 
> A notice from README.md:
> 
> ````ssh` is solely used here to allocate a pseudo-tty to make the ncurses-based UI work properly.
> 
> **There is no ssh jailbreak, Linux pentesting, username bruteforcing**, etc. involved in this challenge.
> 
> If you waste your time doing so, it will be considered an attack on server infrastructure && consequently a _valid reason for disqualification_.```

Hint 1: You may want to try compiling & running the program yourself; the binary given was compiled without Rust's default debug features.

Hint 2: You probably don't want to write a script for this one.

Hint 3: The challenge `simple` was released at the same time for a reason.

### Turbo Fast Crypto, part 2

Points: 900
Solves: 1
Author: main

Flag: 

#### Description

> Using the key you extracted, we found a (link)[https://drive.google.com/uc?id=19mmImjpreALZSs0D88BtLY65cFBkHsMC&export=download] to the source code for turbofastcrypto. There happens to be a secret flag file on the server, and you need to extract it.
> 
> **A first blood prize of one (1) month of Discord Nitro is available for this challenge.**
> 
> (the target server is the same as part 1)

Hint 1: find a way to execute print_flag()

Hint 2: you will probably want some kind of disassembler/debugger for this. Googlable software: Binary Ninja, Ghidra, gdb

## CRYPTO

### Shalom Shalom

Points: 50
Solves: 55
Author: noyou

Flag: IRS{cryptographyiscool}

#### Description

> AT least my mom will let me play cake BASH with my friends if i finish my cryptography homework, can you help me decode it:
> xibkgltizksbrhxllo
> wrap the flag header around the decoded message, i.e. IRS{decoded_message}

Hint 1: The hint is in the description

### Turbo Fast Crypto, part 1

Points: 117
Solves: 29
Author: main

Flag: IRS{secrets_are_revealed!!}

#### Description

> We found the frontend code for a remote encryption service at `nc challs.sieberrsec.tech 3477`:
>
> ```python
> import turbofastcrypto # The source code for this module is only available for part 2 of this challenge :)
> while 1:
>     plaintext = input('> ')
>     ciphertext = turbofastcrypto.encrypt(plaintext)
>     print('Encrypted: ' + str(ciphertext))
> ```
>
> My partner says it operates under the hood with "[XOR](https://en.wikipedia.org/wiki/Exclusive_or)", whatever that means. I need you to recover the key.

Hint 1: Reset the connection if you're having trouble.

### I can't open this file? Part 2

Points: 189
Solves: 14
Author: origami10004

Flag: 

#### Description

> Thanks for helping me recover that file, now I have another [file](https://drive.google.com/uc?id=116Rz1ZxPHo8WLLJ2tLEFe3eNNN_Ybc7y&export=download) but it has been [encrypted](https://drive.google.com/file/d/1guL0UY1-QMAeJ6hSiO2TsTixU-7Qb_fJ/view) into something entirely different. Think you can help me again?

### Diffie's Key Exchange

Points: 192
Solves: 27
Author: noyou

Flag: IRS{d1ff1e_h311m4n!!!}

#### Description

> Diffie created a new key exchange system to help securely transfer private keys in a public channel. Can you see whats wrong with his system?
> Connect here: `nc challs.sieberrsec.tech 1337`
> [chall.py](https://drive.google.com/file/d/1eDDjWOaS_LlAheC1GJUqPoethwgI-NWW/view)

Hint 1: Does the name Diffie sound familiar? Goolge is your best friend!!

### I can't open this file? Part 1

Points: 210
Solves: 30
Author: origami10004

Flag: IRS{n0w_y0u_c4n_c0d3}

#### Description

> Oh no, I've encrypted a file and deleted the original! Now I have a [file](https://drive.google.com/uc?id=1RxVhP6RG7sA9pH7cp2a1HGc4nS5YNQ_D&export=download) that is filled with rubbish. Thankfully I still have the encryption [script](https://drive.google.com/file/d/1GIBfeCjmx3qscYDFHuZ9Se2L8NYybk2I/view), help me recover the original file! I'll even give you a flag if you do.

### totallyfoolproofcrypto

Points: 884
Solves: 7
Author: main

Flag: 

#### Description

> In hindsight, rolling my own crypto was a rather stupendous stroke of stupidity. I'll be switching to a [well-known, verified library](https://www.pycryptodome.org/en/latest/) to fix this.
>
> ```python
> from Crypto.Util.Padding import pad,unpad
> from Crypto.Cipher import AES
> import os
> 
> with open("flag", 'rb') as f: flag = f.read().strip()
> key = os.urandom(16)
> 
> while 1:
>     pt = input('> ').encode()
>     padded = pad(pt+flag, AES.block_size)
>     cipher = AES.new(key, AES.MODE_ECB)
>     print(cipher.encrypt(padded).hex())
> ```
>
> `nc challs.sieberrsec.tech 31311`
>
> **A first blood prize of one (1) month of Discord Nitro is available for this challenge.**
>
> Some amount of "bruteforce" will be necessary -- and hence legal -- for this challenge.

Hint 1: You should search for ECB related AES crypto CTF problems; this is a rather common newbie challenge

### Diffie's Key Exchange 2

Points: 895
Solves: 4
Author: noyou

Flag: 

#### Description

> Diffie learnt that his implementation of the system wasn't secure :<< and made some changes. Try it now!
> Connect here: `nc challs.sieberrsec.tech 1338`
> [chall.py](https://drive.google.com/file/d/1u7H3Ej2dv1AsWNKVQXO5EhUOsnVt_zR3/view)

### whodunnit

Points: 895
Solves: 4
Author: seemin

Flag: 

#### Description

> The Association of Criminals, Subversives and Insurgents (ACSI, in short) are big fans of [RSA encryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), and recently published a [list of their members' public keys](https://drive.google.com/uc?id=19mXJh_4NNZQsbGegvEJHF87tnQiQqIKX&export=download). For reasons unbeknownst to us, they have a habit of **signing** their messages with **multiple** private keys before **encrypting** the signed message with a **single** public key.
> 
> Using one of our portable False Base Stations, we [captured](https://drive.google.com/file/d/1eabGvwCiTVRwlYJritB2qXeBvvNGi6J1/view) one of ASCI's **encrypted**, **doubly-signed**, super secret **alphabetic** passwords (along with the public key used to encrypt it). We need you to figure out **who signed the password**, and **what the password** is by decrypting && unsigning the captured RSA transmission.
> 
> Flag format: `IRS{Name of first person to sign_Name of second person to sign_The password}`
> 
> *Challenge description extemporised by @main*

Hint 1: [Encryption: M^e % n = C] [Decryption: C^d % n = M] [Signing: M^d % n = S] [Unsigning S: S^e % n = M]

Hint 2: Obtaining a decryption key (d) is not necessary at any point in this challenge.

Hint 3: try to read the bolded words

## RE

### Flag checker

Points: 50
Solves: 58
Author: main

Flag: IRS{insp3ct_e1ement}

#### Description

> [http://challs.sieberrsec.tech:15231](http://challs.sieberrsec.tech:15231)
> 
> **Note**: There is **no reason** to use bruteforce for this challenge.

Hint 1: right click --> inspect element

### Reverse

Points: 164
Solves: 37
Author: noyou

Flag: IRS{805b41736b4d43ebb15fc1}

#### Description

> Reverse Engineering but in python?!!!
> [reverse.py](https://drive.google.com/file/d/1yhMvtjck8wJ43c8XL7qIJ6-NpKO_28L0/view)

Hint 1: you don't need to reverse the entire script

### Flag checker v2.0

Points: 899
Solves: 2
Author: main

Flag: 

#### Description

> Same interface, another `check_flag()`.
> 
> Easy, right?
> 
> [http://challs.sieberrsec.tech:15232/](http://challs.sieberrsec.tech:15232/)
> 
> **A first blood prize of [any Steam game that costs <= S$15] is available for this challenge.**

Hint 1: https://github.com/WebAssembly/wabt might be a good starting point.

## OSINT

### "The Sieberr" Heist Part 1

Points: 60
Solves: 45
Author: hongxun

Flag: IRS{3_HUNTERRD_BALMORAL_2088_2}

#### Description

> Well, boss instructed me not to reveal much, but we're planning some heist and I need your help.
> 
> One of our men tailed someone to their home quite a while back.
> 
> He discreetly took a quick picture to mark the location of the person's house.
> 
> Please help me determine the location.
> 
> *(Actually, the heist was planned to be carried out sometime then, but due to unforeseen circumstances it was delayed and we are now revisiting the resources we had obtained back then).*
> ---
> Submit the flag as IRS{*A*_*B*_*C*_*D*_*E*}
> where:
> 
> A. Unit Number *(without any spacing and numbers only)*
> 
> B. Street Name *(without any spacing and in all capitals)* [e.g. If the road name is "John Rd", input as "JOHNRD"; "John St" > "JOHNST"]
> 
> C. Locality Name *(without any spacing and in all capitals)*
> 
> D. Postcode *(numbers only)*
> 
> E. Number of Storeys of the House *(without any spacing and numbers only)*
> 
> [the_sieberr_heist_part1.jpg](https://drive.google.com/uc?id=12OAxXXD9aIKnHIffOnKPaoIymXkmiUoc&export=download)
> ---
> Addendum for "The Sieberr" Heist Part 1:
> 
> - A locality is found within the suburb 🙂

### A Wealth of Information Part 1

Points: 69
Solves: 45
Author: xzy_10

Flag: IRS{Apple_f/1.6_5.1mm_OFF_161021_ABOVE}

#### Description

> Found this [picture](https://drive.google.com/uc?id=1YymGZ_5s4Yx1t5gPaJItm7s7_hlITxfs&export=download) from somewhere, and NOW it's YOUR TURN to find something out from it!
> 
> Tell me:
> 
> *A*. Name of the Camera Brand (in PascalCase)
> 
> *B*. The Aperture of the Camera (include "f/")
> 
> *C*. Focal length of the lens (include units without space)
> 
> *D*. Is the flash on or off (ON/OFF)
> 
> *E*. Date at which this picture was taken (DDMMYY)
> 
> *F*. Is the place above or below sea level (ABOVE/BELOW)
> ---
> Submit the flag as follows:
> 
> IRS{*A*_*B*_*C*_*D*_*E*_*F*}

Hint 1: It's frankly surprisng as to the amount of information that a camera inputs into an image the moment it was captured. How would you view it?

### We go way back

Points: 85
Solves: 28
Author: bryanbryanbryanbryan

Flag: IRS{IHungry}

#### Description

> My old friends created an app and made a public presentation about it, but they changed the name to something stupid and wont tell me the old one. Could you help me find the old name?
> 
> I managed to get the [google slides](https://docs.google.com/presentation/d/1gXGdoVw9X2YxEdyfTn6Lz0sbmuzCYs8H9zd1EOlJHL4/edit#slide=id.p) they used when creating the slides
> 
> Flag format: IRS{*APPNAME*}
> 
> **A first blood prize of one (1) 500¥ coin is available for this challenge.** (note: delivery time may be significant)

### A Wealth of Information Part 2

Points: 243
Solves: 24
Author: xzy_10

Flag: IRS{589333_ROUTE_2_TELECOM}

#### Description

> Where was I?
> ---
> Submit the flag as follows:
> 
> IRS{*A*_ROUTE_*X*_*B*} without any spacing and all capitals, copying "ROUTE" as is.
> 
> Where:
> 
> A = Postal code of the nearest visitor centre
> 
> B = Name of the closest building to the place
> 
> X = The name of the route/road

### "The Sieberr" Heist Part 3

Points: 286
Solves: 12
Author: hongxun

Flag: IRS{B1_MONAVALE_MONAVALEHOSPITAL}

#### Description

> Alright, there are some new developments and I need your help again.
> 
> The guy's name is Casrihms Myrert, you can find him on social media.
> 
> He's going to a hospital to visit someone's kid, but we hear that there is another person that he will be visiting in the same hospital. This other person is of interest to us.
> 
> Let me know what hospital he is going to, as well as what bus he is taking.
> ---
> Submit the flag as IRS{*A*_*B*_*C*}
> 
> A. Bus route number *(any letter should be in capitals)*
> 
> B. Destination of the bus route that the bus is heading to *(without any spacing and in all capitals)*
> 
> C. Name of the hospital that our guy is going to *(without any spacing and in all capitals)*

### "The Sieberr" Heist Part 2

Points: 333
Solves: 22
Author: hongxun

Flag: IRS{YORKST_DRUITTST_VOLVO_B12BLEA_BONDIJUNCTION}

#### Description

> We retrieved this photo from the person's phone.
> 
> How did we get it? You don't need to know, don't be silly and ask too many questions.
> 
> Anyway, the IT team commented that the guy seemed particularly interested in this photo. Unfortunately though, they were not able to find more info.
> 
> Tell me as much information as you can deduce from this photo.
> ---
> Submit the flag as IRS{*A*_*B*_*C*_*D*_*E*_*F*}
> where:
> 
> A. Name of the street that the photo was taken on *(without any spacing and in all capitals)* [e.g. If the road name is "John Rd", input as "JOHNRD"; "John St" > "JOHNST"]
> 
> B. Name of the cross street *(without any spacing and in all capitals)* [e.g. If the road name is "John Rd", input as "JOHNRD"; "John St" > "JOHNST"]
> 
> C. Bus manufacturer *(without any spacing and in all capitals)*
> 
> D. Bus model *(without any spacing and in all capitals)*
> 
> E. Bus route number *(any letter should be in capitals)*
> 
> F. Destination of the bus route that the bus is heading to *(without any spacing and in all capitals)*
> 
> [the_sieberr_heist_part2.png](https://drive.google.com/uc?id=1wWRyMCzW7iLMf73hFHahdmvtwqce9NlU&export=download)

### Public Transport Hunt

Points: 380
Solves: 21
Author: xzy_10

Flag: IRS{22599_EW27_609961}

#### Description

> My friend stole my $10 book voucher and camera away and took these [pictures](https://drive.google.com/uc?id=118gSQvIpzGt5CtCxNcbYD_89eZvpuAc4&export=download) of bus stops and train stations...
> 
> I have absolutely no idea where he is now.
> 
> Help me trace the sly path of his scheming thievery and get my voucher back!
> 
> You might even get the voucher if you are fast enough...
> ---
> Submit the flag as IRS{*A*_*B*_*C*}
> 
> Where:
> 
> A = Bus stop code of the bus stop he was at in the first image
> 
> B = MRT station code (include line code without spacing) in the second image
> 
> C = Postal code of the building right beside the bus stop he was at in the third image
> 
> **A first blood prize of one $10 POPULAR/Kinokuniya voucher is available for this challenge.**

## WEB

### [Part 1] FUTURE TECHNOLOGIES AI IOT FOURTH INDUSTRIAL REVOLUTION SECURITY CAMERA

Points: 62
Solves: 44
Author: theoleecj

Flag: IRS{w4y_t00_eZ_1nJ3c710n}

#### Description

> In our recent investigations, Siebersec got hold of a
> 
> ***FUTURE TECHNOLOGIES AI IOT FOURTH INDUSTRIAL REVOLUTION SECURITY CAMERA*** .
> 
> We suspect that it's yet another one of those vulnerable IoT devices with a web interface that's basically asking to be attacked.
> 
> Try logging in as a camera viewer.
> 
> [http://challs.sieberrsec.tech:4896](http://challs.sieberrsec.tech:4896)

### [Part 2] FUTURE TECHNOLOGIES AI IOT FOURTH INDUSTRIAL REVOLUTION SECURITY CAMERA

Points: 76
Solves: 35
Author: theoleecj

Flag: IRS{7h3_In73rn37_0f_vULn3erable_7hIng5}

#### Description

> In our recent investigations, Siebersec got hold of a
> 
> ***FUTURE TECHNOLOGIES AI IOT FOURTH INDUSTRIAL REVOLUTION SECURITY CAMERA*** .
> 
> I think that the camera is intentionally pointed away from something we need to see.
> 
> Find a way to rotate the camera (pan the camera) and let us see more things.
> 
> [http://challs.sieberrsec.tech:4896](http://challs.sieberrsec.tech:4896)

### TaiYang IT Solution Part 1

Points: 470
Solves: 13
Author: theoleecj

Flag: IRS{g00g13_s1gn_1n_d035nt_m3aN_y0uR3_sAf3}

#### Description

> TaiYang IT Solution offers a variety of services, including one that is put behind a ***supposedly*** secure Google Log In. However, I heard that it uses... ***questionable*** validation code.
> 
> Log in as the admin, and get the flag! Challenge is here: [http://challs.sieberrsec.tech:30593/](http://challs.sieberrsec.tech:30593/)
> 
> Source provided: [http://dl.sieberrsec.tech/608fe2851fbf907e0b15c2cecdad5316886013b8581446af879ccaf6/sctf2021-jwt.7z](http://dl.sieberrsec.tech/608fe2851fbf907e0b15c2cecdad5316886013b8581446af879ccaf6/sctf2021-jwt.7z)
> 
> You'll need 7zip to open the archive. If you don't have it, [download it](https://www.7-zip.org/download.html).
> 
> 

Hint 1: Open your browser's Developer Tools!

Hint 2: There are more easily-bypassable "security" measures hidden in the portal than the code might suggest.

### Exploring The Universe! (Part 1)

Points: 479
Solves: 7
Author: willi123yao

Flag: IRS{1nT3rP1anet4rY_F1L3_sYs8emz}

#### Description

> Everyone knows about the big universe that surrounds us, where all of us use daily to retrieve latest information and hottest news from all over the world! It is of course, no other than, the one and only, Internet!
> 
> To access files and information on the Internet, we all use a protocol called Internet Protocol (IP). This facilitates locating resources throughout the entire network and finds the best way to the destination.
> 
> Come on, its 2021! We are moving everything to the decentralised and distributed, away from all those central organisations! There are so many newer and very revolutionary protocols developed to share information on the web other than common protocols such as HTTPS and FTP.
> 
> Now enough of introductions.
> 
> Agent Myat is working on a university project to explore the massive decentralised universe and has some juicy information hidden there!
> However, he is being very tight-lipped about it and we only managed to get these information from him:
> 
> `QmZ15yK5GE7gKzKSNC2yj9nLWwNH7sbgyyFcE8pSvzSLMQ`
> 
> `k51qzi5uqu5dgrhngvuucsfv4mqmg8btaxhc8zg20ojwfpyl9gcb08ek4381it`
> 
> Locate his hidden project and unveal his findings to everyone!

### TaiYang IT Solution Part 2: Electric Boogaloo

Points: 895
Solves: 4
Author: theoleecj

Flag: IRS{a77rac71ng_y0uR_aUD13nc3}

#### Description

> After the initial vulnerability disclosure, TaiYang IT Solution employed a new cybersecurity specialist to secure their systems which used Google Sign-In.
> 
> They were complaining about how their support staff would just login with the company Google Account to any website they received in their Inbox! How terrible!
> 
> Challenge is here (part 2!): [http://challs.sieberrsec.tech:30593/](http://challs.sieberrsec.tech:30593/) (see Admin Panel Modern)
> 
> *This challenge may require you to setup a Google Firebase Project.*
> 
> *This challenge may require you to send emails (you could use Gmail, or Outlook, anything really).*
> 
> Source provided: [http://dl.sieberrsec.tech/608fe2851fbf907e0b15c2cecdad5316886013b8581446af879ccaf6/sctf2021-jwt.7z](http://dl.sieberrsec.tech/608fe2851fbf907e0b15c2cecdad5316886013b8581446af879ccaf6/sctf2021-jwt.7z)
> 
> ^ source is slightly modified from original
> 
> **A first blood prize of one (1) $10 GrabGifts Card is available for this challenge.**

## FORENSICS

### Duck Delivery

Points: 77
Solves: 34
Author: ditzchann

Flag: IRS{H1dD3n_dUck}

#### Description

> I ordered duck for dinner but all I got was an empty box! Can you help me find where it went?
> [DuckBox.jpg](https://drive.google.com/file/d/1R2UPgI_In6rRmSvafxLjzqpfP4jY3LQC/view?usp=sharing)

Hint 1: Files can contain other files.

### Birds?

Points: 114
Solves: 30
Author: ditzchann

Flag: IRS{s0m3Th1n9_5ouNDs_w3iRd}

#### Description

> I can't help but feel that the birds are trying to tell me something...
> [suspiciousbirds.mp3](https://drive.google.com/file/d/1kFnY_osLBB9AEnnyYeZFCaowVXhrPLZL/view?usp=sharing)

Hint 1: you may want to google for other instances of mp3 files in CTFs

### Digging In The Dump Pt. I

Points: 266
Solves: 31
Author: taiz2000

Flag: IRS{D1ggiNg_1N_tH3_chR0M3_h15t0rY}

#### Description

> Our friend, Alex, used to visit a website, but ever since his computer died the url to the website was lost!
> The only hope now lies in his old hard drive, which was salvaged from his pc
> Hopefully something useful can be found
> 
> Here is a dump of his %APPDATA% folder
> Can you help him find the website?
> [Download Link](http://dl.sieberrsec.tech/08c7d9ff90b7ad86214f020394612af2394e0b28fb73e93d1beaa34e/AppData.zip)

Hint 1: You might want to use a SQLite Browser

### Digging In The Dump Pt. II

Points: 292
Solves: 9
Author: taiz2000

Flag: IRS{aL1_uR_p45sw0rD_4r3_b3LOnG_t0_u5}

#### Description

> After finding that website, perhaps you can find the saved credentials to login to his account?
> (Using the same file in Pt. I)
> 
> Computer username: `Alex`
> Computer password: `Password1`
> (These are NOT the login credentials for the website)
> 
> This challenge is eligible for First Blood prize worth $10, contact @Taiz2000 on Discord if you first blood this challenge.

### Mind Cracking Adversity

Points: 299
Solves: 4
Author: xzy_10

Flag: IRS{M1N3VI3W3R}

#### Description

> My thumbdrive got corrupted and all I have left of my /saves folder is this [world](https://drive.google.com/u/0/uc?id=1xb61Dac98oTIPMOjYnK0C7PY-nfwIblQ&export=download) here...
> 
> Help me find out what I built inside!
> 
> Note: If you are unable to see the words clearly, open a ticket and show a proof that you found it.

### Exploring The Universe! (Part 2)

Points: 382
Solves: 5
Author: willi123yao

Flag: IRS{G3TT1NG-G00D-1S-the-WAY-T0-5UCC35S!}

#### Description

> Oh noes! It seems like Agent Myat has some rather fun teammates, and theres something they're trying to hide!
> 
> Look for the clues and try to uncover what he has been doing lately.
> 
> Remember, nothing is really deleted on the Internet.
> 
> **First blood prize for this challenge is either 1 month Spotify Premium or $10 Starbucks eGift**

### plush, lush, flush, blush

Points: 688
Solves: 7
Author: xzy_10

Flag: IRS{plu5h_15_f1u5h_0n_th3_gr0und}

#### Description

> ok so there's this plush that i really want from pokemon centre but there's no more physical stock left. :(
> so, i had it delivered in paper mario style instead!
> [can you find the hidden message?](https://drive.google.com/uc?id=1V_iJCuBS7jTWICh3qxwJwdEChyh4mAzq&export=download)

## MISC

### Heads and Tails Part 1

Points: 50
Solves: 50
Author: hongxun

Flag: IRS{Got_Head_Got_Tail_YAY_Y0u_W1nnEd_tH1S_G4m3!}

#### Description

> ![](https://i.imgur.com/wb9ixch.png)
> 
> Get the ***Heads and Tails***
> then you **win**!
> 
> [heads_and_tails_part1.jpg](https://drive.google.com/uc?id=1cGCXeXE6tVDQQ1lbrQzZKO48h9kknleK&export=download)

### Heads and Tails Part 2

Points: 73
Solves: 37
Author: hongxun

Flag: IRS{w0w_you_aRe_a_proed_4t_tH1s}

#### Description

> Again..! But it seems that it's **heads** to win this time. (and a 50-cent coin)
> 
> [heads_and_tails_part2.jpg](https://drive.google.com/uc?id=1CYDspO2-x04B866SDfFb5RVgY9czFUtV&export=download)

### Heads and Tails Part 3

Points: 163
Solves: 25
Author: hongxun

Flag: IRS{a_cLOwN_H1dd3N_aT_Le_T4iL}

#### Description

> Yet again..! (this time with a dollar coin)
> 
> If you finish this, I will give you a GIFt :)
> 
> [heads_and_tails_part3.jpg](https://drive.google.com/uc?id=1b_SeVviqcV2tVr-gRu1lgOgUbJew7Mj2&export=download)

Hint 1: 46 69 6C 65 20 73 69 67 6E 61 74 75 72 65 73

### Can You Math It?

Points: 313
Solves: 25
Author: taiz2000

Flag: IRS{4f2cd85d0a9f32f4}

#### Description

> Can you solve 100 math equations?
> 
> What if you only have 5 seconds to solve each?
> 
> Server source code available [here](http://dl.sieberrsec.tech/98756fb6a159147b590437ac13ec5b98a9de9b44945b76a0c4384600/Can%20You%20Math%20It.py)
> 
> [This is a scripting challenge. You are expected to write a script to solve it.]
> 
> Connect to the challenge at `nc challs.sieberrsec.tech 29079`

Hint 1: Don't try to do it by hand. Don't.

### I lost my anime collection! Pt. II

Points: 398
Solves: 4
Author: taiz2000

Flag: IRS{b4D_p4rT1tION_tAb13}

#### Description

> One of the drives on my computer just went missing!
> It's definitely still in my computer, but I can't find it anywhere in Windows
> Can you help me again?
> [Download Link](http://dl.sieberrsec.tech/5b1a1d016fb842ad18bf20b3813649a0038f6971dac37d6100ca181b/I%20lost%20my%20anime%20collection%21%20Pt.%20II.zip)
> 
> This challenge is eligible for First Blood prize worth $10, contact @Taiz2000 on Discord if you first blood this challenge.

### I lost my anime collection! Pt. I

Points: 500
Solves: 2
Author: taiz2000

Flag: 

#### Description

> One of the hard drives in my NAS just died!
> I heard that it's in RAID 5, whatever that means..
> Can you help me recover my beloved files?
> Here's the remaining drives
> [Download](http://dl.sieberrsec.tech/c5284026f68163625f8e3afeec4529316a6b15f89f971d58e6d39c24/I%20lost%20my%20anime%20collection%21%20Pt.%20I.zip)

Hint 1: You might want to use VMWare Player. It's free!

Hint 2: A consumer version of Windows can't read RAID 5!

### rock farming simulator deluxe edition

Points: 600
Solves: 0
Author: main

Flag: 

#### Description

> *DLC unlocked: pony pathfinding & more!*
> 
> `ssh -p 33251 rock_farming_simulator@challs.sieberrsec.tech`

## SANITY

### sanity check

Points: 50
Solves: 58
Author: main

Flag: IRS{th@nk_y0u_for_r3ading!}

#### Description

> 🤔

