export default class BaseClass {
  constructor (list = []) {
    this.list = list
  }

  clearAndAddItems (list) {
    this.clear()
    this.addItems(list)
  }

  addItems (list) {
    list.forEach(item => this.addItem(item))
  }

  clear () {
    this.list = []
  }

  deleteItem (id) {
    let findIndex = this.findIndex(id)
    if (findIndex > -1) {
      this.list.splice(findIndex, 1)
    }
  }

  findIndex (id) {
    return this.list.findIndex(o => o.id === id)
  }

  findItem (id) {
    return this.list.find(o => o.id === id)
  }

}