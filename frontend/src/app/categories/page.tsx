"use client";
import { useState, useEffect } from "react";

type CountData = {
  total_questions?: number;
  total_topics?: number;
};

export default function Index() {
  const [countData, setCountData] = useState<CountData>({});

  useEffect(() => {
    const fetchAndSetCounts = async () => {
      try {
        const countUrl = process.env.NEXT_PUBLIC_COUNT_URL;
        if (!countUrl) {
          throw new Error(
            "NEXT_PUBLIC_COUNT_URL environment variable is not set"
          );
        }
        const response = await fetch(countUrl, {
          method: "GET",
        });
        const data = await response.json();
        // Check if data exists
        if (data !== undefined) {
          setCountData(data);
        } else {
          // Optional: Handle cases where data is null
          console.warn("Data is null");
        }
      } catch (error) {
        // Optional: Error handling for the getData() call
        console.error("Failed to fetch categories:", error);
      }
    };

    fetchAndSetCounts(); // Call the async function immediately
  }, []); // The empty dependency array ensures this runs only once on mount

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <div className=" bg-gradient-to-r from-purple-600 to-indigo-800">
        <div className="container mx-auto px-4 py-10">
          <div className="max-w-4xl mx-auto text-center text-white">
            <h1 className="text-5xl font-black mb-4">
              Explore <span className="text-amber-400">Categories</span>
            </h1>
            <p className="text-xl mb-8 max-w-2xl mx-auto">
              Discover thousands of trivia questions across diverse topics. From
              history to science, find your passion and challenge your
              knowledge.
            </p>
            <div className="flex flex-wrap justify-center gap-4 text-sm">
              <div className="flex items-center gap-2 bg-white/10 backdrop-blur-sm px-4 py-2 rounded-full">
                {/* <Zap className="h-4 w-4 text-accent-400" /> */}
                <span>{countData["total_questions"]}+ Questions</span>
              </div>
              <div className="flex items-center gap-2 bg-white/10 backdrop-blur-sm px-4 py-2 rounded-full">
                {/* <Globe className="h-4 w-4 text-accent-400" /> */}
                <span>{countData["total_topics"]} Categories</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
