var Year = function(input) {
    this.value = input;
};

Year.prototype.isLeap = function() {
    if (this.value % 400 == 0 || (this.value % 4 == 0 && this.value % 100 != 0)) return true;
    else return false;
};

module.exports = Year;