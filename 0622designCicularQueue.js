class MyCircularQueue {
  constructor(k) {
    this.q = Array(k).fill(0);
    this.len = 0;
    this.cap = k;
    this.head = 0;
    this.tail = -1;
  }

  enQueue(value) {
    if (this.isFull()) return false;

    if (this.tail === this.cap - 1) {
      this.tail = 0;
    } else {
      ++this.tail;
    }
    this.q[this.tail] = value;
    this.len++;
    return true;
  }

  deQueue() {
    if (this.isEmpty()) return false;

    if (this.head === this.cap - 1) {
      this.head = 0;
    } else {
      ++this.head;
    }
    this.len--;
    return true;
  }

  Front() {
    if (this.len === 0) return -1;
    return this.q[this.head];
  }

  Rear() {
    if (this.len === 0) return -1;
    return this.q[this.tail];
  }

  isEmpty() {
    return this.len === 0;
  }

  isFull() {
    return this.len === this.cap;
  }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
