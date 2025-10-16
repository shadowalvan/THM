Challenge:
Navigate to the following to tackle the question for the task:
While testing the cart workflow I intercepted the Add to cart / Update cart request in Burp, modified the item price from 100 to 10, forwarded the request, then applied coupon DISCOUNT10 and completed checkout. The order was accepted at the tampered price — demonstrating insufficient server-side validation of price/coupon and allowing attackers to pay less than intended.
**Vulnerability**
**Insecure direct object/parameter manipulation — price integrity not enforced on the server.**
The application trusts price information supplied by the client (HTTP request body/parameters). An attacker can modify the price parameter before it reaches the server and the server will accept it and process an order using the supplied value.
Root cause: server relies on client-supplied price rather than deriving item price from a trusted server-side source (database, product catalog) or using signed prices.
I added item to cart and captured the request on burpsuite
<img width="774" height="772" alt="image" src="https://github.com/user-attachments/assets/8e00fdab-4aba-4b8b-ab0b-7f865bf06b27" />
I changed the price from 100 to 10 and forwarded the request
<img width="675" height="861" alt="image" src="https://github.com/user-attachments/assets/67ee7b6a-ad11-4c81-aee3-873545d28d19" />

Price changed on the cart successfully
<img width="1390" height="385" alt="image" src="https://github.com/user-attachments/assets/5e7064c4-ec7b-4123-81d9-3699c57a7589" />

I applied the coupon DISCOUNT10 and purchased 
<img width="604" height="843" alt="image" src="https://github.com/user-attachments/assets/3fee2c9d-d406-4f45-afd2-05539db35bc5" />

Pawned successfully
<img width="883" height="277" alt="image" src="https://github.com/user-attachments/assets/835c9e03-b882-4d88-8de3-736500805701" />
**Impact**
Attackers can purchase items for less (financial loss).
Coupon stacking / abuse may be possible (apply coupons after lowering price).
Reputational / business loss if exploited at scale.

