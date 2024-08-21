function claculateDiscountedPrice(price, discountPercentage){
    const discount = (price * discountPercentage) / 100
    const priceWithDiscoun = price - discount
    return priceWithDiscoun
}

const originalPrice = 100
const discountPercentage = 20
const finalPrice = claculateDiscountedPrice(originalPrice, discountPercentage)

console.log(`Original Price: $${originalPrice}%`);
console.log(`Discount: ${discountPercentage}%`);
console.log(`Price with discount: $${finalPrice}`);

