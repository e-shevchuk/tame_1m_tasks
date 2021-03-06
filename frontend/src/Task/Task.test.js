import Task from "../Task";
import {allEvents, allTasks} from '../App.test_data'
import Event from "../Event";
import moment from "moment";

test('Constructor', ()=>{

  const t = new Task()

  expect(t).toBeInstanceOf(Task)
})

test('Simple properties', ()=>{

  const t = new Task()
  const data = {...allTasks[288]}

  t.title = data.title
  t.pinned = data.pinned
  t.complete = data.complete
  t.duration = 7200000

  expect(t.title).toBe(data.title)
  expect(t.pinned).toBe(data.pinned)
  expect(t.complete).toBe(data.complete)
  expect(t.duration).toBe(7200000)
})

test('fromDBJSON() 0101', ()=>{
  const dataWhole = {...allTasks[288]}
  const json = JSON.stringify(dataWhole)
  const task = Task.fromDBJSON(json)
  // ID
  expect(task.id).toBe(288)
  //Title
  expect(task.title).toBe('288 Redirect & all the sh*t')
  // Duration
  expect(task.duration).toBe(7200000)
  // Data from DB
  expect(task.dataDB.id).toBe(288)
})

test('fromDBJSON() 0202', ()=>{
  const msg = "Task.initByDB(): 'id' is not exists"

  const dataWhole = {...allTasks[288]}
  delete dataWhole.id
  const json = JSON.stringify(dataWhole)

  expect.assertions(1)
  try {
    const task = Task.fromDBJSON(json)
  } catch (e) {
    expect(e.message).toBe(msg)
  }
})