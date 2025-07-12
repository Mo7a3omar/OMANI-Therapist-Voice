"""
Cultural Appropriateness Validator for Omani Arabic Responses
"""

from test_cases_omani import get_omani_expressions, get_inappropriate_responses
from typing import Dict, List, Any

class OmaniCulturalValidator:
    """Validates cultural appropriateness of AI responses for Omani context"""
    
    def __init__(self):
        self.omani_expressions = get_omani_expressions()
        self.inappropriate_responses = get_inappropriate_responses()
        
    def validate_response(self, response: str, context: str = "General") -> Dict[str, Any]:
        """Comprehensive cultural validation of AI response"""
        
        validation_result = {
            'overall_score': 0.0,
            'omani_authenticity': 0.0,
            'religious_sensitivity': 0.0,
            'cultural_appropriateness': True,
            'inappropriate_content': [],
            'missing_elements': [],
            'recommendations': []
        }
        
        # Check for inappropriate content
        inappropriate_found = []
        for inappropriate in self.inappropriate_responses:
            if inappropriate in response:
                inappropriate_found.append(inappropriate)
                validation_result['cultural_appropriateness'] = False
        
        validation_result['inappropriate_content'] = inappropriate_found
        
        # Check for Omani authenticity
        omani_score = 0
        found_expressions = []
        
        for category, expressions in self.omani_expressions.items():
            for expr in expressions:
                if expr in response:
                    omani_score += 1
                    found_expressions.append(expr)
        
        validation_result['omani_authenticity'] = min(omani_score / 3, 1.0)  # Normalize to 0-1
        
        # Check religious sensitivity
        religious_score = 0
        religious_expressions = self.omani_expressions.get('religious_context', [])
        for expr in religious_expressions:
            if expr in response:
                religious_score += 1
        
        validation_result['religious_sensitivity'] = min(religious_score / 2, 1.0)
        
        # Generate recommendations
        if validation_result['omani_authenticity'] < 0.5:
            validation_result['missing_elements'].append("Authentic Omani expressions")
            validation_result['recommendations'].append("Add expressions like: شلونك، ما عليك، بإذن الله")
        
        if validation_result['religious_sensitivity'] < 0.3 and context in ["Spiritual", "Religious"]:
            validation_result['missing_elements'].append("Islamic context")
            validation_result['recommendations'].append("Add appropriate religious expressions")
        
        if inappropriate_found:
            validation_result['recommendations'].append("Remove culturally inappropriate expressions")
        
        # Calculate overall score
        validation_result['overall_score'] = (
            validation_result['omani_authenticity'] * 0.4 +
            validation_result['religious_sensitivity'] * 0.3 +
            (1.0 if validation_result['cultural_appropriateness'] else 0.0) * 0.3
        )
        
        return validation_result
    
    def test_cultural_validation_suite(self) -> Dict[str, Any]:
        """Run comprehensive cultural validation tests"""
        
        test_responses = [
            {
                'response': "شلونك؟ أفهم مشاعرك، ما عليك، بإذن الله الأمور راح تتحسن",
                'context': "General",
                'expected_score': 0.8
            },
            {
                'response': "الله يعينك في هذا الوقت الصعب، توكل على الله وكله راح يكون زين",
                'context': "Spiritual",
                'expected_score': 0.9
            },
            {
                'response': "حرام عليك تحس كذا، هذا عيب منك",
                'context': "General",
                'expected_score': 0.0
            },
            {
                'response': "I understand your feelings, everything will be okay",
                'context': "General",
                'expected_score': 0.3
            }
        ]
        
        results = []
        for test in test_responses:
            validation = self.validate_response(test['response'], test['context'])
            results.append({
                'response': test['response'],
                'context': test['context'],
                'validation_result': validation,
                'expected_score': test['expected_score'],
                'passed': abs(validation['overall_score'] - test['expected_score']) < 0.3
            })
        
        # Summary
        passed_tests = sum(1 for r in results if r['passed'])
        total_tests = len(results)
        
        return {
            'test_results': results,
            'summary': {
                'total_tests': total_tests,
                'passed_tests': passed_tests,
                'success_rate': passed_tests / total_tests * 100,
                'average_score': sum(r['validation_result']['overall_score'] for r in results) / total_tests
            }
        }

# Example usage
if __name__ == "__main__":
    validator = OmaniCulturalValidator()
    
    # Test individual response
    test_response = "شلونك؟ أفهم قلقك، ما عليك، بإذن الله كله راح يكون زين"
    result = validator.validate_response(test_response)
    
    print("Cultural Validation Results:")
    print(f"Overall Score: {result['overall_score']:.2f}/1.0")
    print(f"Omani Authenticity: {result['omani_authenticity']:.2f}/1.0")
    print(f"Religious Sensitivity: {result['religious_sensitivity']:.2f}/1.0")
    print(f"Culturally Appropriate: {'Yes' if result['cultural_appropriateness'] else 'No'}")
    
    if result['recommendations']:
        print("\nRecommendations:")
        for rec in result['recommendations']:
            print(f"   • {rec}")
    
    # Run full test suite
    print("\n" + "="*50)
    print("Running Cultural Validation Test Suite")
    
    suite_results = validator.test_cultural_validation_suite()
    print(f"\nSummary:")
    print(f"Total Tests: {suite_results['summary']['total_tests']}")
    print(f"Passed: {suite_results['summary']['passed_tests']}")
    print(f"Success Rate: {suite_results['summary']['success_rate']:.1f}%")
    print(f"Average Score: {suite_results['summary']['average_score']:.2f}/1.0")
