/**
 * @param {Function} fn
 */
function memoize(fn) {
    let hashset = {};
    return function(...args) {
        if (args.length == 2) {
            let key = args[0].toString() + "," + args[1].toString();
            console.log(hashset[key]);
            if (hashset[key] === undefined) {
                let value = fn(...args);
                hashset[key] = value;
                return value;
            } else {
                return hashset[key];
            }
        } else {
            let key = args[0];
            if (hashset[key] === undefined) {
                let value = fn(...args);
                hashset[key] = value;
                return value;
            } else {
                return hashset[key];
            }
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */