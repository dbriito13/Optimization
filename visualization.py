from manim import *


class pathwise_coordinate_visualization(MovingCameraScene,Scene):
    def construct(self):

        problem_equation = MathTex(
            r"\min_{\beta} \left [ \frac{1}{2} \left | \left | y-X\beta \right | \right |_{2}^{2} + \lambda \left | \left | \beta \right | \right |_{1} \right ]"
        ).scale(1.5)
        self.add(problem_equation)
        self.play(Write(problem_equation))
        self.wait()

        self.play(
            self.camera.frame.animate.set_width(problem_equation.width * 3)
        )

        self.play(ApplyMethod(problem_equation.shift, 5 * UP))

        beta = MathTex(r"\beta")
        lambdaa = MathTex(r"\lambda")
        beta_description = Text(" : vector of models")
        lambdaa_description = Text(" : penalty parameter")

        params_beta = (
            VGroup(beta, beta_description).arrange(RIGHT).shift(3 * UP)
        )
        params_lambda = (
            VGroup(lambdaa, lambdaa_description)
            .arrange(RIGHT)
            .shift(UP * 1.5)
            .align_to(params_beta, LEFT)
        )

        self.add(params_beta)
        self.play(Write(params_beta))
        self.wait()

        self.add(params_lambda)
        self.play(Write(params_lambda))
        self.wait()

        problem_to_solve = Tex(
            "We will use the pathwise coordinate method proposed by Jerome Friedman, Trevor Hastie, "
            "Holger Höfling and Robert Tibshirani in their research paper publisehd in 2007 "
            "to approximate the solution for this equation",
            substrings_to_isolate=["pathwise coordinate method"],
        ).shift(1.5*DOWN)
        problem_to_solve.set_color_by_tex("pathwise coordinate method", YELLOW)

        self.add(problem_to_solve)
        self.play(Write(problem_to_solve))
        self.wait()
