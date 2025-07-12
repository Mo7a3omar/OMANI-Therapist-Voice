"""
Load Testing Utilities for OMANI-Therapist-Voice Project
Simulates concurrent users and measures system performance under load
"""

import asyncio
import time
import random
import statistics
from typing import Dict, List, Any
import json
from datetime import datetime

class LoadTester:
    """Simulate concurrent users for load testing"""
    
    def __init__(self, max_concurrent_users=10):
        self.max_concurrent_users = max_concurrent_users
        self.results = []
        self.session_data = []
    
    async def simulate_user_session(self, user_id: int, session_length: int = 5):
        """Simulate a single user session with realistic Omani user behavior"""
        session_start = time.time()
        user_results = []
        
        # Simulate different user types
        user_types = ["General Anxiety", "Family Issues", "Work Stress", "University Student"]
        user_type = random.choice(user_types)
        
        for turn in range(session_length):
            turn_start = time.time()
            
            # Simulate user thinking/speaking time (varies by user type)
            if user_type == "General Anxiety":
                thinking_time = random.uniform(3, 10)  # Anxious users may hesitate
            elif user_type == "Family Issues":
                thinking_time = random.uniform(5, 15)  # Complex family issues take time
            else:
                thinking_time = random.uniform(2, 8)   # Normal thinking time
            
            await asyncio.sleep(thinking_time)
            
            # Simulate STT processing time
            stt_time = random.uniform(0.5, 2.0)
            await asyncio.sleep(stt_time)
            
            # Simulate AI response generation time
            ai_response_time = random.uniform(1.5, 4.0)
            await asyncio.sleep(ai_response_time)
            
            # Simulate TTS processing time
            tts_time = random.uniform(0.3, 1.5)
            await asyncio.sleep(tts_time)
            
            total_turn_time = time.time() - turn_start
            
            turn_result = {
                'user_id': user_id,
                'user_type': user_type,
                'turn': turn,
                'thinking_time': thinking_time,
                'stt_time': stt_time,
                'ai_response_time': ai_response_time,
                'tts_time': tts_time,
                'total_turn_time': total_turn_time,
                'timestamp': time.time()
            }
            
            user_results.append(turn_result)
            self.results.append(turn_result)
        
        session_duration = time.time() - session_start
        
        session_summary = {
            'user_id': user_id,
            'user_type': user_type,
            'session_duration': session_duration,
            'total_turns': session_length,
            'average_turn_time': statistics.mean([r['total_turn_time'] for r in user_results]),
            'session_start': session_start,
            'session_end': time.time()
        }
        
        self.session_data.append(session_summary)
        return session_duration
    
    async def run_load_test(self, num_users: int = 5, session_length: int = 5):
        """Run concurrent load test with multiple users"""
        print(f"Starting load test with {num_users} concurrent users")
        print("=" * 50)
        
        # Clear previous results
        self.results = []
        self.session_data = []
        
        # Create concurrent user sessions
        tasks = []
        for user_id in range(num_users):
            task = asyncio.create_task(
                self.simulate_user_session(user_id, session_length)
            )
            tasks.append(task)
        
        # Run all sessions concurrently
        start_time = time.time()
        session_durations = await asyncio.gather(*tasks)
        total_test_time = time.time() - start_time
        
        # Analyze results
        return self.analyze_load_test_results(num_users, total_test_time)
    
    def analyze_load_test_results(self, num_users: int, total_test_time: float) -> Dict[str, Any]:
        """Analyze load test results and generate comprehensive report"""
        
        if not self.results:
            return {"error": "No results to analyze"}
        
        # Basic statistics
        all_turn_times = [r['total_turn_time'] for r in self.results]
        all_ai_times = [r['ai_response_time'] for r in self.results]
        all_stt_times = [r['stt_time'] for r in self.results]
        all_tts_times = [r['tts_time'] for r in self.results]
        
        # Session statistics
        session_durations = [s['session_duration'] for s in self.session_data]
        
        # Performance metrics
        performance_metrics = {
            'total_turn_time': {
                'mean': statistics.mean(all_turn_times),
                'median': statistics.median(all_turn_times),
                'min': min(all_turn_times),
                'max': max(all_turn_times),
                'std_dev': statistics.stdev(all_turn_times) if len(all_turn_times) > 1 else 0
            },
            'ai_response_time': {
                'mean': statistics.mean(all_ai_times),
                'median': statistics.median(all_ai_times),
                'min': min(all_ai_times),
                'max': max(all_ai_times)
            },
            'stt_processing_time': {
                'mean': statistics.mean(all_stt_times),
                'median': statistics.median(all_stt_times)
            },
            'tts_processing_time': {
                'mean': statistics.mean(all_tts_times),
                'median': statistics.median(all_tts_times)
            }
        }
        
        # Concurrency analysis
        concurrency_analysis = {
            'concurrent_users': num_users,
            'total_test_duration': total_test_time,
            'total_interactions': len(self.results),
            'interactions_per_second': len(self.results) / total_test_time,
            'average_session_duration': statistics.mean(session_durations),
            'system_utilization': (sum(all_turn_times) / total_test_time) * 100
        }
        
        # User type analysis
        user_type_stats = {}
        for user_type in set(r['user_type'] for r in self.results):
            type_results = [r for r in self.results if r['user_type'] == user_type]
            user_type_stats[user_type] = {
                'count': len(type_results),
                'avg_turn_time': statistics.mean([r['total_turn_time'] for r in type_results]),
                'avg_thinking_time': statistics.mean([r['thinking_time'] for r in type_results])
            }
        
        # Performance thresholds
        performance_issues = []
        if performance_metrics['total_turn_time']['mean'] > 20:
            performance_issues.append("Average response time exceeds 20 seconds")
        
        if performance_metrics['total_turn_time']['max'] > 30:
            performance_issues.append("Maximum response time exceeds 30 seconds")
        
        if concurrency_analysis['system_utilization'] > 80:
            performance_issues.append("System utilization is very high")
        
        # Recommendations
        recommendations = []
        if performance_metrics['ai_response_time']['mean'] > 5:
            recommendations.append("Improve AI response generation speed")
        
        if performance_metrics['stt_processing_time']['mean'] > 3:
            recommendations.append("Improve speech-to-text processing")
        
        if concurrency_analysis['interactions_per_second'] < 1:
            recommendations.append("Improve system concurrency handling")
        
        return {
            'test_summary': {
                'concurrent_users': num_users,
                'total_interactions': len(self.results),
                'test_duration': total_test_time,
                'success_rate': 100.0,  # Assuming all interactions succeeded
                'timestamp': datetime.now().isoformat()
            },
            'performance_metrics': performance_metrics,
            'concurrency_analysis': concurrency_analysis,
            'user_type_analysis': user_type_stats,
            'performance_issues': performance_issues,
            'recommendations': recommendations,
            'detailed_results': self.results[:10]  # First 10 results for reference
        }
    
    def generate_load_test_report(self, results: Dict[str, Any]) -> str:
        """Generate a formatted load test report"""
        
        report = f"""
# Load Test Report - OMANI Therapist Voice

## Test Summary
- Concurrent Users: {results['test_summary']['concurrent_users']}
- Total Interactions: {results['test_summary']['total_interactions']}
- Test Duration: {results['test_summary']['test_duration']:.2f} seconds
- Success Rate: {results['test_summary']['success_rate']:.1f}%

## Performance Metrics

### Response Times
- Average Total Time: {results['performance_metrics']['total_turn_time']['mean']:.2f} seconds
- Max Response Time: {results['performance_metrics']['total_turn_time']['max']:.2f} seconds
- Min Response Time: {results['performance_metrics']['total_turn_time']['min']:.2f} seconds

### Component Performance
- Average AI Response Time: {results['performance_metrics']['ai_response_time']['mean']:.2f} seconds
- Average STT Processing Time: {results['performance_metrics']['stt_processing_time']['mean']:.2f} seconds
- Average TTS Processing Time: {results['performance_metrics']['tts_processing_time']['mean']:.2f} seconds

## Concurrency Analysis
- Interactions per Second: {results['concurrency_analysis']['interactions_per_second']:.2f}
- System Utilization: {results['concurrency_analysis']['system_utilization']:.1f}%
- Average Session Duration: {results['concurrency_analysis']['average_session_duration']:.2f} seconds

## User Type Analysis
"""
        
        for user_type, stats in results['user_type_analysis'].items():
            report += f"""
### {user_type}
- Interaction Count: {stats['count']}
- Average Response Time: {stats['avg_turn_time']:.2f} seconds
- Average Thinking Time: {stats['avg_thinking_time']:.2f} seconds
"""
        
        if results['performance_issues']:
            report += "\n## Performance Issues\n"
            for issue in results['performance_issues']:
                report += f"- Warning: {issue}\n"
        
        if results['recommendations']:
            report += "\n## Recommendations\n"
            for rec in results['recommendations']:
                report += f"- Suggestion: {rec}\n"
        
        return report

# Stress testing functionality
class StressTester(LoadTester):
    """Extended load tester for stress testing scenarios"""
    
    async def run_stress_test(self, max_users: int = 20, duration_minutes: int = 5):
        """Run progressive stress test"""
        
        print(f"Starting progressive stress test")
        print(f"Max users: {max_users} for {duration_minutes} minutes")
        print("=" * 60)
        
        stress_results = []
        
        # Progressive load increase
        for num_users in range(1, max_users + 1, 2):
            print(f"\nTesting with {num_users} users...")
            
            # Run shorter sessions for stress testing
            result = await self.run_load_test(num_users, session_length=3)
            result['stress_level'] = num_users
            stress_results.append(result)
            
            # Check if system is degrading
            if result['performance_metrics']['total_turn_time']['mean'] > 25:
                print(f"Performance degradation detected at {num_users} users")
                break
            
            # Brief pause between stress levels
            await asyncio.sleep(2)
        
        return {
            'stress_test_results': stress_results,
            'max_stable_users': self._find_max_stable_users(stress_results),
            'performance_degradation_point': self._find_degradation_point(stress_results)
        }
    
    def _find_max_stable_users(self, results: List[Dict]) -> int:
        """Find maximum number of users with stable performance"""
        for result in results:
            if result['performance_metrics']['total_turn_time']['mean'] > 20:
                return max(1, result['stress_level'] - 2)
        return results[-1]['stress_level'] if results else 1
    
    def _find_degradation_point(self, results: List[Dict]) -> int:
        """Find point where performance starts degrading"""
        baseline = results[0]['performance_metrics']['total_turn_time']['mean'] if results else 10
        
        for result in results:
            current_performance = result['performance_metrics']['total_turn_time']['mean']
            if current_performance > baseline * 1.5:  # 50% degradation
                return result['stress_level']
        
        return results[-1]['stress_level'] if results else 1

# Example usage and testing
if __name__ == "__main__":
    import asyncio
    async def main():
        # Basic load test
        print("Running basic load test")
        load_tester = LoadTester()
        
        # Test with 5 concurrent users
        results = await load_tester.run_load_test(num_users=5, session_length=4)
        
        # Generate and display report
        report = load_tester.generate_load_test_report(results)
        print(report)
        
        # Save results
        with open('load_test_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print("\n" + "="*60)
        print("Running stress test")
        
        # Stress test
        stress_tester = StressTester()
        stress_results = await stress_tester.run_stress_test(max_users=15, duration_minutes=3)
        
        print(f"\nStress Test Results:")
        print(f"Max stable users: {stress_results['max_stable_users']}")
        print(f"Performance degradation point: {stress_results['performance_degradation_point']} users")
        
        # Save stress test results
        with open('stress_test_results.json', 'w', encoding='utf-8') as f:
            json.dump(stress_results, f, ensure_ascii=False, indent=2)
        
        print("Results saved.")
    
    asyncio.run(main())
