import time
import asyncio
import logging
import statistics
from datetime import datetime
from typing import List, Dict, Any
import json
from test_cases_omani import get_omani_test_cases, get_omani_expressions

class PerformanceMetrics:
    """Class to track and analyze performance metrics"""
    
    def __init__(self):
        self.metrics = {
            'stt_latency': [],
            'ai_response_latency': [],
            'tts_latency': [],
            'total_latency': [],
            'response_quality': [],
            'crisis_detection_accuracy': [],
            'cultural_appropriateness': [],
            'omani_authenticity': []
        }
    
    def add_metric(self, metric_type: str, value: float):
        if metric_type in self.metrics:
            self.metrics[metric_type].append(value)
    
    def get_statistics(self, metric_type: str) -> Dict[str, float]:
        if metric_type not in self.metrics or not self.metrics[metric_type]:
            return {}
        
        values = self.metrics[metric_type]
        return {
            'mean': statistics.mean(values),
            'median': statistics.median(values),
            'min': min(values),
            'max': max(values),
            'std_dev': statistics.stdev(values) if len(values) > 1 else 0
        }

class OmaniTherapistTester:
    """Main testing class for the OMANI-Therapist-Voice project"""
    
    def __init__(self):
        self.metrics = PerformanceMetrics()
        self.test_results = []
        self.logger = logging.getLogger(__name__)
        self.omani_expressions = get_omani_expressions()
        
    def simulate_stt_processing(self, audio_length: float) -> tuple:
        """Simulate Speech-to-Text processing with Omani Arabic"""
        start_time = time.time()
        # Realistic STT processing time for Arabic
        processing_time = audio_length * 0.4 + 0.6  # Slightly longer for Arabic
        time.sleep(processing_time)
        end_time = time.time()
        
        return "Transcribed text from audio", end_time - start_time
    
    def simulate_gemini_response(self, user_input: str, history: List) -> tuple:
        """Simulate Gemini AI response generation with Omani context"""
        start_time = time.time()
        
        # Crisis detection with Omani keywords
        crisis_keywords = [
            "انتحار", "أموت", "أنهي حياتي", "ما فيني أعيش",
            "تعبت من الحياة", "ما عاد فيني", "خلاص تعبت"
        ]
        is_crisis = any(keyword in user_input for keyword in crisis_keywords)
        
        # Simulate processing time
        if is_crisis:
            processing_time = 1.0  # Crisis responses are immediate
            response_type = "crisis"
            ai_response = "I hear you're going through a very difficult time. Contact support immediately: +968-2205-5555"
        elif len(user_input.split()) > 25:
            processing_time = 3.0  # Complex queries
            response_type = "complex"
            ai_response = "I understand your feelings, this is natural. Let's work together on this, God willing things will improve"
        else:
            processing_time = 2.0  # Normal response
            response_type = "normal"
            ai_response = "How are you? I understand your feelings, don't worry, God willing everything will be fine"
        
        time.sleep(processing_time)
        end_time = time.time()
        
        return ai_response, response_type, end_time - start_time
    
    def simulate_tts_processing(self, text: str) -> tuple:
        """Simulate Text-to-Speech processing for Arabic"""
        start_time = time.time()
        
        # Arabic TTS typically takes longer
        text_length = len(text)
        processing_time = (text_length / 80) * 0.6 + 0.4  # Adjusted for Arabic
        time.sleep(processing_time)
        end_time = time.time()
        
        return b'mock_arabic_audio_data', end_time - start_time
    
    def evaluate_cultural_appropriateness(self, response: str) -> float:
        """Evaluate cultural appropriateness of response"""
        score = 0
        
        # Check for Omani expressions
        for category, expressions in self.omani_expressions.items():
            for expr in expressions:
                if expr in response:
                    score += 1
        
        # Normalize score (0-1)
        max_possible_score = 5  # Reasonable maximum
        return min(score / max_possible_score, 1.0)
    
    def run_single_test(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Run a single test case and measure performance"""
        test_start = time.time()
        
        print(f"   Testing: {test_case['name']}")
        print(f"   Input: {test_case['input_text'][:50]}...")
        
        # Step 1: STT Processing
        transcribed_text, stt_latency = self.simulate_stt_processing(
            test_case.get('audio_length', 3.0)
        )
        
        # Step 2: AI Response Generation
        ai_response, response_type, ai_latency = self.simulate_gemini_response(
            test_case['input_text'], 
            test_case.get('history', [])
        )
        
        # Step 3: TTS Processing
        audio_bytes, tts_latency = self.simulate_tts_processing(ai_response)
        
        total_latency = time.time() - test_start
        
        # Evaluate cultural appropriateness
        cultural_score = self.evaluate_cultural_appropriateness(ai_response)
        
        # Record metrics
        self.metrics.add_metric('stt_latency', stt_latency)
        self.metrics.add_metric('ai_response_latency', ai_latency)
        self.metrics.add_metric('tts_latency', tts_latency)
        self.metrics.add_metric('total_latency', total_latency)
        self.metrics.add_metric('cultural_appropriateness', cultural_score)
        
        # Test result
        result = {
            'test_case': test_case['name'],
            'input_text': test_case['input_text'],
            'cultural_context': test_case.get('cultural_context', 'General Omani'),
            'transcribed_text': transcribed_text,
            'ai_response': ai_response,
            'response_type': response_type,
            'stt_latency': stt_latency,
            'ai_latency': ai_latency,
            'tts_latency': tts_latency,
            'total_latency': total_latency,
            'cultural_score': cultural_score,
            'meets_requirement': total_latency < 20.0,
            'timestamp': datetime.now().isoformat()
        }
        
        self.test_results.append(result)
        return result
    
    def run_performance_suite(self, test_cases: List[Dict]) -> Dict[str, Any]:
        """Run complete performance test suite"""
        print("Starting OMANI-Therapist-Voice Performance Tests")
        print("=" * 70)
        
        for i, test_case in enumerate(test_cases, 1):
            print(f"\nTest {i}/{len(test_cases)}: {test_case['name']}")
            result = self.run_single_test(test_case)
            
            # Print results
            status = "PASS" if result['meets_requirement'] else "FAIL"
            print(f"   Total Latency: {result['total_latency']:.2f}s {status}")
            print(f"   STT: {result['stt_latency']:.2f}s | AI: {result['ai_latency']:.2f}s | TTS: {result['tts_latency']:.2f}s")
            print(f"   Cultural Score: {result['cultural_score']:.2f}/1.0")
        
        return self.generate_performance_report()
    
    def generate_performance_report(self) -> Dict[str, Any]:
        """Generate comprehensive performance report"""
        report = {
            'test_summary': {
                'total_tests': len(self.test_results),
                'passed_tests': sum(1 for r in self.test_results if r['meets_requirement']),
                'failed_tests': sum(1 for r in self.test_results if not r['meets_requirement']),
                'success_rate': 0,
                'average_cultural_score': 0
            },
            'performance_metrics': {},
            'cultural_analysis': {},
            'recommendations': []
        }
        
        # Calculate success rate
        if report['test_summary']['total_tests'] > 0:
            report['test_summary']['success_rate'] = (
                report['test_summary']['passed_tests'] / 
                report['test_summary']['total_tests'] * 100
            )
            
            # Calculate average cultural score
            cultural_scores = [r['cultural_score'] for r in self.test_results]
            report['test_summary']['average_cultural_score'] = statistics.mean(cultural_scores)
        
        # Performance statistics
        for metric_type in ['stt_latency', 'ai_response_latency', 'tts_latency', 'total_latency', 'cultural_appropriateness']:
            report['performance_metrics'][metric_type] = self.metrics.get_statistics(metric_type)
        
        # Cultural analysis
        crisis_tests = [r for r in self.test_results if r['response_type'] == 'crisis']
        normal_tests = [r for r in self.test_results if r['response_type'] == 'normal']
        
        report['cultural_analysis'] = {
            'crisis_detection_accuracy': len(crisis_tests) / len([t for t in get_omani_test_cases() if 'أموت' in t['input_text'] or 'انتحار' in t['input_text']]) if crisis_tests else 0,
            'normal_response_quality': statistics.mean([r['cultural_score'] for r in normal_tests]) if normal_tests else 0,
            'omani_authenticity': report['test_summary']['average_cultural_score']
        }
        
        # Generate recommendations
        total_stats = report['performance_metrics']['total_latency']
        if total_stats and total_stats['mean'] > 15:
            report['recommendations'].append("Consider optimizing AI response generation for faster performance")
        
        if total_stats and total_stats['max'] > 20:
            report['recommendations'].append("Some test cases exceed 20s requirement - investigate edge cases")
        
        if report['test_summary']['average_cultural_score'] < 0.7:
            report['recommendations'].append("Needs improvement in using authentic Omani expressions")
        
        return report

# Main execution
if __name__ == "__main__":
    # Initialize tester
    tester = OmaniTherapistTester()
    
    # Get Omani test cases
    test_cases = get_omani_test_cases()
    
    # Run performance suite
    performance_report = tester.run_performance_suite(test_cases)
    
    # Display detailed report
    print("\n" + "="*70)
    print("PERFORMANCE REPORT")
    print("="*70)
    
    print(f"\nTest Summary:")
    print(f"   Total Tests: {performance_report['test_summary']['total_tests']}")
    print(f"   Passed: {performance_report['test_summary']['passed_tests']}")
    print(f"   Failed: {performance_report['test_summary']['failed_tests']}")
    print(f"   Success Rate: {performance_report['test_summary']['success_rate']:.1f}%")
    print(f"   Average Cultural Score: {performance_report['test_summary']['average_cultural_score']:.2f}/1.0")
    
    print(f"\nPerformance Metrics:")
    for metric, stats in performance_report['performance_metrics'].items():
        if stats:
            metric_name = metric.replace('_', ' ').title()
            print(f"   {metric_name}:")
            print(f"      Mean: {stats['mean']:.2f}s")
            print(f"      Min/Max: {stats['min']:.2f}s / {stats['max']:.2f}s")
    
    print(f"\nCultural Analysis:")
    cultural = performance_report['cultural_analysis']
    print(f"   Crisis Detection Accuracy: {cultural['crisis_detection_accuracy']:.1%}")
    print(f"   Normal Response Quality: {cultural['normal_response_quality']:.2f}/1.0")
    print(f"   Omani Authenticity: {cultural['omani_authenticity']:.2f}/1.0")
    
    if performance_report['recommendations']:
        print(f"\nRecommendations:")
        for rec in performance_report['recommendations']:
            print(f"   • {rec}")
    
    # Save results to file
    with open('omani_performance_results.json', 'w', encoding='utf-8') as f:
        json.dump(performance_report, f, ensure_ascii=False, indent=2)
    
    print(f"\nResults saved to: omani_performance_results.json")
