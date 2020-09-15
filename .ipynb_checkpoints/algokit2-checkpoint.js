// return transpose of matrix, rows, and columns of a matrix

class Matrix {
  constructor(matrix) {
    this.matrix = matrix.split('\n').map(row => row.split(' ').map(Number));
  }

  get transpose() {
    return this.rows[0].map((_,i) => this.rows.map(v => v[i]));
  }

  get rows() {
    return this.matrix;
  }

  get cols() {
    return this.transpose;
  }
}

let matrix = new Matrix('1 2 3\n4 5 6\n7 8 9\n8 7 6');
console.log(matrix);
console.log(matrix.transpose);
console.log(matrix.rows[3]);
console.log(matrix.cols[1]);