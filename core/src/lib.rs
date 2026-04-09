use pyo3::prelude::*;

#[pyclass]
#[derive(Clone)]
struct Vector {
    data: Vec<f64>,
}

#[pymethods]
impl Vector {
    #[new]
    fn new(data: Vec<f64>) -> Self {
        Vector { data }
    }

    fn __repr__(&self) -> String {
        format!("{:?}", self.data)
    }

    fn add(&self, other: &Vector) -> PyResult<Vector> {
        if self.data.len() != other.data.len() {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Vectors must have the same length",
            ));
        }

        let result: Vec<f64> = self
            .data
            .iter()
            .zip(other.data.iter())
            .map(|(a, b)| a + b)
            .collect();

        Ok(Vector { data: result })
    }

    fn dot(&self, other: &Vector) -> PyResult<f64> {
        if self.data.len() != other.data.len() {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Vectors must have the same length",
            ));
        }

        let result: f64 = self
            .data
            .iter()
            .zip(other.data.iter())
            .map(|(a, b)| a * b)
            .sum();

        Ok(result)
    }

    fn __add__(&self, other: Vector) -> PyResult<Vector> {
        self.add(&other)
    }
}

#[pymodule]
fn core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Vector>()?;
    Ok(())
}
