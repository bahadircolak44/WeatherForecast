import BaseClass from './BaseClass'

export class CityList extends BaseClass {
  addItem (data) {
    let newItem = new City(data)
    this.list.push(newItem)
  }
}

export class City {
  constructor (data = {}) {
    this.id = data.id || null
    this.city_name = data.city_name || null
  }
}
