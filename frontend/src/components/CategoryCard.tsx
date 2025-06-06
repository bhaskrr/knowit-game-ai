import { CircleHelp } from "lucide-react";

interface Category {
  name: string;
  question_count: number;
  description: string;
}

export function CategoryCard(category: Category) {
  return (
    <div className="group relative px-6 py-6 bg-gradient-to-br from-purple-50 via-white to-blue-50 rounded-3xl shadow-xl hover:shadow-2xl transition-all duration-300 cursor-pointer overflow-hidden border border-gray-100 hover:border-purple-300 transform hover:-translate-y-2">
      <div className="flex items-center gap-3">
        <div className="bg-purple-100 p-3 rounded-full shadow-md group-hover:bg-purple-200 transition">
          <CircleHelp className="text-purple-500 text-2xl" />
        </div>
        <h3 className="text-xl font-extrabold text-gray-800 group-hover:text-purple-700 transition">
          {category.name}
        </h3>
      </div>
      <p className="mt-3 text-sm font-medium text-gray-600 flex items-center gap-2">
        <span className="inline-block bg-blue-100 text-blue-700 px-2 py-1 rounded-full font-semibold text-xs shadow-sm">
          {category.question_count} Questions
        </span>
      </p>
      <p className="mt-4 text-gray-500 text-base">{category.description}</p>
      <a
        className="mt-6 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg bg-gradient-to-r from-purple-500 to-blue-500 text-white px-4 py-2 shadow-lg hover:from-purple-600 hover:to-blue-600 transition focus:outline-none focus:ring-2 focus:ring-purple-400"
        href="#"
      >
        Explore
        <svg className="w-4 h-4" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" />
        </svg>
      </a>
      <div className="absolute -top-8 -right-8 w-32 h-32 bg-purple-100 rounded-full opacity-30 group-hover:scale-110 transition-transform duration-300"></div>
    </div>
  );
}