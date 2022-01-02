# WEP security flaws

1. RC4 algorithm weaknesses due to the key construction - RC4(K || IV) with || meaning concatenation

2. IVs are too short

3. CRC32 isn't cryptographically secure due to its linearity

4. No built-in method of updating keys
