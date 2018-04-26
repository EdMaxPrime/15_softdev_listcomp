#Return true if atleast one number, lowercase, and uppercase letter
def password_minimally_safe(pword):
    return len([c for c in pword if c >= 'A' and c <= 'Z'][:1] + [c for c in pword if c >= 'a' and c <= 'z'][:1] + [c for c in pword if c >= '0' and c <= '9'][:1]) >= 3

print password_minimally_safe("") #no
print password_minimally_safe("a") #no
print password_minimally_safe("aZ") #no
print password_minimally_safe("1z") #no
print password_minimally_safe("Z1") #no
print password_minimally_safe("N0o") #yes
print password_minimally_safe("jhaBBINUI2992kjdewiOIbBUOB") #yes

#Utility: returns a list like range() does but with chars
def crange(low, high):
    return [chr(i) for i in range(ord(low), ord(high) + 1)]

#Returns a password's strength rating on a scale of 1-10, where 1 is weak and 10 is strong
#1 point for trying, [0, 2] points for lowercase, [0, 2] points for uppercase, [0, 2] points for numbers, [0, 2] points for special characters, and 1 point for password lengths > 8
def password_strength(pword):
    score = 1
    score += len([c for c in pword if c in crange('0', '9')][:2])
    score += len([c for c in pword if c in crange('a', 'z')][:2])
    score += len([c for c in pword if c in crange('A', 'Z')][:2])
    score += len([c for c in pword if c in ".?!@#$%^&*-=+_;:,/"][:2])
    score += 1 if len(pword) > 8 else 0
    return score

print password_strength("") #1
print password_strength("a") #2
print password_strength("abc") #3
print password_strength("abc123") #5
print password_strength("aa11AA&%") #9
print password_strength("jhaBBINUI2992kjdewiOIbBUOB__") #10