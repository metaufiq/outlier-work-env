const axios = require('axios');

const createUser = async (name, reps, weight, unit, date) => {
  const url = `http://localhost:3000/create?name=${name}&reps=${reps}&weight=${weight}&unit=${unit}&date=${date}`;
  try {
    const response = await axios.get(url);
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
};

const users = [
  { name: 'squat', reps: 10, weight: 33, unit: 'lbs', date: '11/1/2121' },
  { name: 'bench press', reps: 8, weight: 50, unit: 'lbs', date: '11/2/2121' },
  { name: 'deadlift', reps: 6, weight: 60, unit: 'lbs', date: '11/3/2121' },
  { name: 'overhead press', reps: 12, weight: 25, unit: 'lbs', date: '11/4/2121' },
  { name: 'barbell row', reps: 10, weight: 40, unit: 'lbs', date: '11/5/2121' },
];

(async () => {
  for (const user of users) {
    await createUser(user.name, user.reps, user.weight, user.unit, user.date);
  }
})();