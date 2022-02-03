import VueRouter from 'vue-router';
import HomePage from './Pages/HomePage';
import Category from './Pages/Category';
import CategoryForm from './Pages/CategoryForm';

const routes = [
  { path: '/', component: HomePage, name: 'HomePage' },
  { path: '/categories/:cat_id', component: Category, name: 'Category' },
  { path: '/categoryform', component: CategoryForm, name: 'CategoryForm' }
];

export default new VueRouter({ routes, mode: 'history' });
