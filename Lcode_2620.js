
var createCounter = function(n) { 
    let count = n; 
    return function() { 
        return count++; 
    }; 
}; 

const counter = createCounter(10); // Fixed the typo 'creator Counter'

console.log(counter()); // 10
console.log(counter()); // 11
console.log(counter()); // 12
console.log(counter()); // 13 (Fixed: call 'counter()' instead of 'count()')

