import { Button } from "@/components/ui/button";
import Image from "next/image";
import Link from "next/link";
// import { Brain, Sparkles, Zap } from "lucide-react";

export const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 via-blue-600 to-indigo-800 overflow-hidden">
      {/* Background decorative elements */}
      {/* <div className="absolute inset-0">
        <div className="absolute top-20 left-10 w-32 h-32 bg-yellow-400 rounded-full opacity-20 animate-pulse"></div>
        <div className="absolute bottom-32 right-20 w-24 h-24 bg-pink-400 rounded-full opacity-20 animate-pulse delay-1000"></div>
        <div className="absolute top-1/2 left-1/4 w-16 h-16 bg-green-400 rounded-full opacity-20 animate-pulse delay-500"></div>
      </div> */}

      <div className="container mx-auto px-4 text-center relative z-10">
        <div className="max-w-4xl mx-auto">
          {/* Logo/Brand */}
          <div className="flex items-center justify-center mb-6">
            <div className="relative bg-yellow-500 rounded-full p-2">
              <Image src="/lightbulb.png" height={70} width={70} alt="logo" />
            </div>
            <h1 className="text-6xl font-bold text-white ml-4 bg-gradient-to-r from-yellow-400 to-orange-400 bg-clip-text text-transparent">
              Know<span className="text-amber-400">It</span>
            </h1>
          </div>

          {/* Main headline */}
          <h2 className="text-4xl md:text-6xl font-bold text-white mb-6 leading-tight">
            AI-Powered Trivia
            {/* <span className="block text-yellow-400">That Adapts to You</span> */}
          </h2>

          {/* Subtitle */}
          <p className="text-xl md:text-2xl text-blue-100 mb-8 max-w-3xl mx-auto">
            Generate trivia questions on any topic.<br/>
            Challenge your mind with quizzes powered by AI.
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
            <div className="flex flex-col sm:flex-row items-center justify-center gap-6 mt-8">
              <Button
                size="lg"
                className="
            px-6 py-6        /* Padding */
            rounded-full       /* Rounded corners */
            font-bold        /* Bold text */
            text-lg          /* Large text */
            transition-all duration-300 ease-in-out /* Smooth transitions for hover */
            cursor-pointer   /* Indicates clickable */
            shadow-lg hover:shadow-xl hover:-translate-y-1 /* Hover effects */

            /* Primary Button Colors */
            bg-amber-400 text-neutral-900 /* Gold background, dark text */
            hover:bg-amber-300           /* Slightly lighter gold on hover */
       "
              >
                <Link href="#">Get Started</Link>
              </Button>

              <Button
                className="
            px-6 py-6        /* Padding */
            rounded-full       /* Rounded corners */
            font-bold        /* Bold text */
            text-lg          /* Large text */
            transition-all duration-300 ease-in-out /* Smooth transitions for hover */
            cursor-pointer   /* Indicates clickable */
            shadow-md hover:shadow-lg hover:-translate-y-1 /* Hover effects */

            bg-indigo-800 text-white    /* Deep indigo background, white text */
            hover:bg-indigo-700         /* Slightly lighter indigo on hover */
       "
              >
                <Link href="/categories">Explore Categories</Link>
              </Button>
            </div>
          </div>

          {/* Stats */}
          {/* <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-2xl mx-auto">
            <div className="text-center">
              <div className="text-3xl font-bold text-yellow-400">∞</div>
              <div className="text-blue-100">Questions Generated</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-yellow-400">50+</div>
              <div className="text-blue-100">Categories</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-yellow-400">AI</div>
              <div className="text-blue-100">Powered</div>
            </div>
          </div> */}
        </div>
      </div>
    </section>
  );
};
