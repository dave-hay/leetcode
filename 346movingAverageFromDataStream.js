/**
 * @param {number} size
 */

class MovingAverage {
  constructor(size) {
    this.size = size;
    this.len = 0;
    this.sum = 0;
    this.q = [];
  }
  next(val) {
    if (this.len < this.size) {
      this.len++;
      this.tail++;
      this.q.push(val);
      this.sum += val;
      return this.sum / this.len;
    } else {
      let old = this.q.shift();
      this.q.push(val);
      this.sum += val - old;
      return this.sum / this.size;
    }
    this.size += val;
    return this.size;
  }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */
